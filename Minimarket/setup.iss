[Setup]
AppName=rls
AppVersion=1.0.1
DefaultDirName={pf}\rls
DefaultGroupName=rls
OutputDir=.
OutputBaseFilename=rlsSetup
SetupIconFile=C:\Users\maria\Desktop\proyectos\Minimarket\Minimarket\archivos_py\resources\r.ico

[Files]
Source: "dist\rls.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\updater.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "archivos_py\resources\r.ico"; DestDir: "{app}\archivos_py\resources"; Flags: ignoreversion
Source: "archivos_py\resources\eye_visible_hide_hidden_show_icon_145988.png"; DestDir: "{app}\archivos_py\resources"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\rls"; Filename: "{app}\rls.exe"; WorkingDir: "{app}"; IconFilename: "{app}\archivos_py\resources\r.ico"
Name: "{commonstartup}\rls"; Filename: "{app}\rls.exe"; WorkingDir: "{app}"; IconFilename: "{app}\archivos_py\resources\r.ico"
Name: "{group}\rls"; Filename: "{app}\rls.exe"; WorkingDir: "{app}"; IconFilename: "{app}\archivos_py\resources\r.ico"