Name:           testtask
Version:        1.0 
Release:        1%{?dist}
Summary:        Test task for RAIDIX

License:        GPL            
Source0:        %{name}-%{version}.tar.gz

BuildRequires: gcc

%description
Simple C++ "Hello World" program for RAIDIX test task.

%prep
%{__rm} -rf %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
%{__tar} -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version}


%build
cd %{name}-%{version}
%{__make}


%install
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{_bindir}
%{__make} install


%clean
%{__rm} -rf $RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_DIR/*

%files
%defattr (-,root,root)
%{_bindir}/%{name}

%changelog
* Sun Nov 13 2022 builder
- 
