﻿/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

import { CodeModelAz } from "./CodeModelAz"
import { HeaderGenerator } from "./Header";
import { ToMultiLine } from "../../utils/helper"

export function GenerateAzureCliInit(model: CodeModelAz): string[] {
    let header: HeaderGenerator = new HeaderGenerator();
    header.addFromImport(model.CliCoreLib, ["AzCommandsLoader"]);
    var output: string[] = header.getLines();
    let importPath = "azext_" + model.Extension_NameUnderscored;
    if (model.IsCliCore) {
        importPath = "";
    }
    output.push("from " + importPath + ".generated._help import helps  # pylint: disable=unused-import");
    output.push("try:");
    output.push("    from " + importPath + ".manual._help import helps  # pylint: disable=reimported");
    output.push("except ImportError:");
    output.push("    pass");
    output.push("");
    output.push("");
    output.push("class " + model.Extension_NameClass + "CommandsLoader(AzCommandsLoader):");
    output.push("");
    output.push("    def __init__(self, cli_ctx=None):");
    output.push("        from " + model.CliCoreLib + ".commands import CliCommandType");
    output.push("        from " + importPath + ".generated._client_factory import cf_" + model.Extension_NameUnderscored + "_cl");
    output.push("        " + model.Extension_NameUnderscored + "_custom = CliCommandType(");
    if (model.IsCliCore) {
        output.push("            operations_tmpl='azure.cli.command_modules." + model.Extension_NameUnderscored + ".custom#{}',");
    } else {
        output.push("            operations_tmpl='azext_" + model.Extension_NameUnderscored + ".custom#{}',");
    }
    output.push("            client_factory=cf_" + model.Extension_NameUnderscored + "_cl)");
    output.push(`        parent = super(${model.Extension_NameClass}CommandsLoader, self)`);
    ToMultiLine(`        parent.__init__(cli_ctx=cli_ctx, custom_command_type=${model.Extension_NameUnderscored}_custom)`, output);
    output.push("");
    output.push("    def load_command_table(self, args):");
    output.push("        from " + importPath + ".generated.commands import load_command_table");
    output.push("        load_command_table(self, args)");
    output.push("        try:");
    output.push("            from " + importPath + ".manual.commands import load_command_table as load_command_table_manual");
    output.push("            load_command_table_manual(self, args)");
    output.push("        except ImportError:");
    output.push("            pass");
    output.push("        return self.command_table");
    output.push("");
    output.push("    def load_arguments(self, command):");
    output.push("        from " + importPath + ".generated._params import load_arguments");
    output.push("        load_arguments(self, command)");
    output.push("        try:");
    output.push("            from " + importPath + ".manual._params import load_arguments as load_arguments_manual");
    output.push("            load_arguments_manual(self, command)");
    output.push("        except ImportError:");
    output.push("            pass");
    output.push("");
    output.push("");
    output.push("COMMAND_LOADER_CLS = " + model.Extension_NameClass + "CommandsLoader");
    output.push("");

    return output;
}
