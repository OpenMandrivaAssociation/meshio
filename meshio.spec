%define version 0.2.0
%define release %mkrel 7
%define name    meshio

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Name:        %{name}
Summary:     Library for the loading of 3D model files
Version:     %{version}
Release:     %{release}
License:     LGPL
Group:       System/Libraries
Source:      meshio-%version.tar.bz2
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
rm -rf $RPM_BUILD_ROOT

%setup -n meshio-%version

%build

%configure 

%make

%install

%makeinstall

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README  
%_libdir/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/*.*a
%_libdir/*.so
%_includedir/MeshIO/

