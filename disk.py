####
# Show free disk space in percentage
#from concurrent.futures.process import _ResultItem
from prompt_toolkit import prompt
import wmi

# Precheck hostnames
Precheck1 = 'PMDBA10654'
Precheck2 = 'PMDBA10653'
Precheck3 = 'PMDBA10652'
Precheck4 = 'PMDBS13988'
Precheck5 = 'PMDBA100309'
Precheck6 = 'Pmdba13699'
Precheck7 = 'Pmdba10674'
Precheck8 = 'Pmdba10678'
Precheck9 = 'Pmdba10675'
Precheck10 = 'Pmdba10677'
Precheck11 = 'Pmdba10676'
Precheck12a = 'Pmdba06397'
Precheck12b = 'Pmdba006113'
Precheck13 = 'Pmdba10680'
Precheck14 = 'Pmdba10681'
Precheck15 = 'Pmdba10683'
Precheck16 = 'Pmdba13775'
Precheck17a = 'Pmdba13777'
Precheck17b = 'Mdba06361'

# Customer Service hostnames
CS1 = 'Mdba10656'
CS2 = 'Mdba13778'
CS3 = 'Mdba10261'
CS4 = 'Mdba10265'
CS5 = 'Mdba06394'
CS6 = 'Mdba06369'
CS7 = 'Mdba100310'

print("="*40, "Precheck Disk Information", "="*40)

pc = wmi.WMI (Precheck1)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck1", Precheck1, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck2)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck2", Precheck2, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck3)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck3", Precheck3, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck4)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck4", Precheck4, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck5)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck5", Precheck5, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck6)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck6", Precheck6, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck7)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck7", Precheck7, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck8)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck8", Precheck8, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck9)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck9", Precheck9, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck10)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck10", Precheck10, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck11)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck11", Precheck11, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck12a)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck12a", Precheck12a, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck12b)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck12b", Precheck12b, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck13)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck13", Precheck13, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck14)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck14", Precheck14, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck15)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck15", Precheck15, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck16)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck16", Precheck16, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (Precheck17a)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck17a", Precheck17a, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40)

pc = wmi.WMI (Precheck17b)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("Precheck17b", Precheck17b, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("")

print("="*40, "Customer Service Disk Information", "="*40)

pc = wmi.WMI (CS1)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("CS1", CS1, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (CS2)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("CS2", CS2, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (CS3)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("CS3", CS3, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (CS4)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("CS4", CS4, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (CS5)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("CS5", CS5, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (CS6)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("CS6", CS6, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)

pc = wmi.WMI (CS7)
for disk in pc.Win32_LogicalDisk (DriveType=3):
    print("CS7", CS7, disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) /  float(disk.Size)))
    print("="*40,)