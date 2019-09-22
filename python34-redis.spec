%global pymajor 3
%global pyminor 4
%global pyver %{pymajor}.%{pyminor}
%global __python3 %{_bindir}/python%{pyver}
%global python3_sitelib  %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global srcname redis

Name:           python34-%{srcname}
Version:        2.10.6
Release:        2%{?dist}
Summary:        Python client for Redis key-value store
Group:          Development/Languages
License:        MIT
URL:            https://github.com/andymccurdy/redis-py
Source0:        https://pypi.io/packages/source/r/redis/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python34-devel
Requires:       python34

# Rename from python34u-redis
Provides:       python34u-%{srcname} = %{version}-%{release}
Obsoletes:      python34u-%{srcname} < 2.10.6-2


%description
The Python interface to the Redis key-value store.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --optimize 1 --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES
%license LICENSE
%{python3_sitelib}/*


%changelog
* Sun Sep 22 2019 Carl George <carl@george.computer> - 2.10.6-2
- Rename to python34-redis

* Thu Aug 17 2017 Ben Harper <ben.harper@rackspace.com> - 2.10.6-1.ius
- Latest upstream
- update Source0

* Wed Nov 04 2015 Carl George <carl.george@rackspace.com> - 2.10.5-1.ius
- Latest upstream

* Fri Aug 15 2014 Carl George <carl.george@rackspace.com> - 2.10.3-1.ius
- Latest upstream

* Tue Aug 12 2014 Ben Harper <ben.harper@rackspace.com> - 2.10.2-1.ius
- Latest sources from upstream

* Fri Jul 18 2014 Ben Harper <ben.harper@rackspace.com> - 2.10.1-1.ius
- Latest sources from upstream

* Tue May 13 2014 Carl George <carl.george@rackspace.com> - 2.9.1-1.ius
- Initial port from python33-redis

* Fri Jan 24 2014 Ben Harper <ben.harper@rackspace.com> - 2.9.1-1.ius
- Latest sources from upstream

* Fri Jan 03 2014 Ben Harper <ben.harper@rackspace.com> - 2.9.0-1.ius
- Latest sources from upstream

* Tue Aug 27 2013 Ben Harper <ben.harper@rackspace.com> - 2.8.0-1.ius
- Latest sources from upstream

* Mon Jun 17 2013 Ben Harper <ben.harper@rackspace.com> - 2.7.6-1.ius
- Latest sources from upstream

* Tue May 14 2013 Ben Harper <ben.harper@rackspace.com> - 2.7.5-1.ius
- Update to 2.7.5

* Mon Apr 29 2013 Ben Harper <ben.harper@rackspace.com> - 2.7.4-1.ius
- Update to 2.7.4
- updated Source0 URL
- remove README.md from %doc

* Tue Apr 23 2013 Ben Harper <ben.harper@rackspace.com> - 2.7.3-1.ius
- Update to 2.7.3

* Mon Mar 04 2013 Ben Harper <ben.harper@rackspace.com> - 2.7.2-1.ius
- Update to 2.7.2

* Tue Oct 16 2012 Ben Harper <ben.harper@rackspace.com> - 2.6.2-1.ius
- Porting from python32-redis

* Mon Sep 24 2012 Ben Harper <ben.harper@rackspace.com> - 2.6.2-1.ius
- Update to 2.6.2

* Thu Sep 20 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 2.6.1-1.ius
- Porting from Fedora rawhide to IUS
- Python 3.x requires 2.6.1 of redis-py 
  https://github.com/andymccurdy/redis-py/issues/259

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 2.4.9-1
- Update to 2.4.9

* Sun Mar 27 2011 Silas Sewell <silas@sewell.ch> - 2.2.4-1
- Update to 2.2.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 04 2010 Silas Sewell <silas@sewell.ch> - 2.0.0-1
- Initial build