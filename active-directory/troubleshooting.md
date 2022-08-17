
# Error

## scripts is disabled on this system

```./enum.ps1
File C:\Users\offsec\Desktop\enum.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.
    + CategoryInfo          : SecurityError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnauthorizedAccess
```


`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

[Reference](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.2)


