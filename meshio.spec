%define debug_package %{nil}
%define version 0.2.0
%define release 10
%define name    meshio

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Name:        %{name}
Summary:     Library for the loading of 3D model files
Version:     %{version}
Release:     %{release}
License:     LGPLv2.1
Group:       System/Libraries
Source:      meshio-%version.tar.bz2
Patch0:      meshio-0.2.0-build.patch

URL:         http://www.3dwm.org/frameset.html


%description 
MeshIO is a simple C++ library for the loading of 3D model 
files. Currently, MeshIO only supports plain .3DS files as 
well as its native .RAW format. MeshIO will undergo a major 
redesign in the future.

%package -n %libname
Summary:     	Library for the loading of 3D model files
Group: 		 System/Libraries

%description -n %libname
MeshIO is a simple C++ library for the loading of 3D model 
files. Currently, MeshIO only supports plain .3DS files as 
well as its native .RAW format. MeshIO will undergo a major 
redesign in the future.


%package -n %libname-devel
Summary:        Library for the loading of 3D model files
Group:          System/Libraries
Requires:	%libname = %version
Provides:	libmeshio-devel

%description -n %libname-devel
MeshIO is a simple C++ library for the loading of 3D model 
files. Currently, MeshIO only supports plain .3DS files as 
well as its native .RAW format. MeshIO will undergo a major 
redesign in the future.


%prep
%setup -n meshio-%version
%patch0 -p0

%build

linux32 ./configure 
%make

%install
%makeinstall



%files -n %libname
%doc AUTHORS COPYING README  
%_libdir/*.so.*

%files -n %libname-devel
%doc AUTHORS COPYING README
%_libdir/*.*a
%_libdir/*.so
%_includedir/MeshIO/

