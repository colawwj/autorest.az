/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
import { EOL } from 'os';
import { isNullOrUndefined } from "util";
import { getLatestPyPiVersion } from '../../../../utils/helper';
import { CodeGenConstants, GenerationMode, PathConstants } from "../../../models";
import { CodeModelAz } from "../../CodeModelAz";
import { HeaderGenerator } from "../../Header";
import { TemplateBase } from "../TemplateBase";
import compareVersions = require('compare-versions');

export class CliExtSetupPy extends TemplateBase {
    constructor(model: CodeModelAz, isDebugMode: boolean) {
        super(model, isDebugMode);
        this.relativePath = PathConstants.setupPyFile;
    }

    public async fullGeneration(): Promise<string[]> {
        return await this.GenerateAzureCliSetupPy(this.model);
    }

    public async incrementalGeneration(base: string): Promise<string[]> {
        if (isNullOrUndefined(base) || base.length == 0) {
            return null;
        }
        else {
            let existingMode: GenerationMode = HeaderGenerator.GetCliGenerationMode(base);
            if (existingMode == GenerationMode.Full) {
                throw new Error("GenerationMode Error: Should not set Incremental mode on existing Full generation RP.");
            }
            else {
                const rst = compareVersions(CodeGenConstants.minCliCoreVersion, "2.3.1");
                if (rst == 0 || rst == 1) {
                    const baseSplit: string[] = base.split(EOL);
                    const headerGenerator: HeaderGenerator = new HeaderGenerator();
                    headerGenerator.generationMode = GenerationMode.Incremental;
                    let output: string[] = headerGenerator.getLines();

                    let firstNoneCommentLineIdx: number = -1;
                    let skipcomment: number = 2;
                    for (let i: number = 0; i < baseSplit.length; ++i) {
                        if (baseSplit[i].startsWith("# ----")) {
                            skipcomment--;
                            if (skipcomment == 0) {
                                firstNoneCommentLineIdx = i;
                                break;
                            }
                        }
                    }
                    if (firstNoneCommentLineIdx != -1) {
                        for (let i: number = firstNoneCommentLineIdx + 1; i < baseSplit.length; ++i) {
                            if (!(baseSplit[i].indexOf("'Programming Language :: Python :: 2',") > -1 
                                || baseSplit[i].indexOf("'Programming Language :: Python :: 2.7',") > -1)) {
                                output.push(baseSplit[i]);
                            }
                        }
                    }
                    return output;
                }
            }
        }
    }

    private async GenerateAzureCliSetupPy(model: CodeModelAz): Promise<string[]> {
        var output: string[] = [];

        output.push("#!/usr/bin/env python");
        output.push("");
        output.push("# --------------------------------------------------------------------------------------------");
        output.push("# Copyright (c) Microsoft Corporation. All rights reserved.");
        output.push("# Licensed under the MIT License. See License.txt in the project root for license information.");
        output.push("# --------------------------------------------------------------------------------------------");
        output.push("");
        output.push("");
        output.push("from codecs import open");
        output.push("from setuptools import setup, find_packages");
        output.push("");
        output.push("# HISTORY.rst entry.");
        output.push("VERSION = '0.1.0'");
        output.push("try:");
        output.push("    from azext_" + model.Extension_NameUnderscored + ".manual.version import VERSION");
        output.push("except ImportError:");
        output.push("    pass");
        output.push("")
        output.push("# The full list of classifiers is available at");
        output.push("# https://pypi.python.org/pypi?%3Aaction=list_classifiers");
        output.push("CLASSIFIERS = [");
        output.push("    'Development Status :: 4 - Beta',");
        output.push("    'Intended Audience :: Developers',");
        output.push("    'Intended Audience :: System Administrators',");
        output.push("    'Programming Language :: Python',");
        output.push("    'Programming Language :: Python :: 3',");
        output.push("    'Programming Language :: Python :: 3.6',");
        output.push("    'Programming Language :: Python :: 3.7',");
        output.push("    'Programming Language :: Python :: 3.8',");
        output.push("    'License :: OSI Approved :: MIT License',");
        output.push("]");
        output.push("");
        if (!model.SDK_NeedSDK) {
            output.push("DEPENDENCIES = [");
            let packageName = model.GetPythonPackageName();
            let latestVersion = await getLatestPyPiVersion(packageName);
            let line = "'" + packageName + "~=" + latestVersion + "'";
            output.push("    " + line)
            output.push("]");
        } else {
            output.push("DEPENDENCIES = []");
        }
        output.push("");

        output.push("try:");
        output.push("    from azext_" + model.Extension_NameUnderscored + ".manual.dependency import DEPENDENCIES");
        output.push("except ImportError:");
        output.push("    pass");
        output.push("");
        output.push("with open('README.md', 'r', encoding='utf-8') as f:");
        output.push("    README = f.read()");
        output.push("with open('HISTORY.rst', 'r', encoding='utf-8') as f:");
        output.push("    HISTORY = f.read()");
        output.push("");
        output.push("setup(");
        output.push("    name='" + model.Extension_NameUnderscored + "',");
        output.push("    version=VERSION,");
        output.push("    description='Microsoft Azure Command-Line Tools " + model.Extension_NameClass + " Extension',");
        output.push("    author='Microsoft Corporation',");
        output.push("    author_email='azpycli@microsoft.com',");
        output.push("    url='https://github.com/Azure/azure-cli-extensions/tree/master/src/" + model.Extension_Name + "',");
        output.push("    long_description=README + '\\n\\n' + HISTORY,");
        output.push("    license='MIT',");
        output.push("    classifiers=CLASSIFIERS,");
        output.push("    packages=find_packages(),");
        output.push("    install_requires=DEPENDENCIES,");
        output.push("    package_data={'azext_" + model.Extension_NameUnderscored + "': ['azext_metadata.json']},");
        output.push(")");
        output.push("");

        return output;
    }
}