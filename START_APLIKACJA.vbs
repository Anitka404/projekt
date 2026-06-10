Set shell = CreateObject("WScript.Shell")
folder = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
shell.CurrentDirectory = folder
shell.Run Chr(34) & folder & "\.venv\Scripts\pythonw.exe" & Chr(34) & " " & Chr(34) & folder & "\main.py" & Chr(34), 1, False
