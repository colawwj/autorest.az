## TEST

``` yaml 
test:
  cli-name: attestation
  test-setup:
    - name: Operations_List
    - name: AttestationProviders_Create
    - name: AttestationProviders_Get
    - function: mytest
    - name: AttestationProviders_List
    - name: AttestationProviders_ListByResourceGroup
    - name: AttestationProviders_Delete
```