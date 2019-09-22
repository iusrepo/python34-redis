%global srcname redis

%if %{undefined el6}
%global __python3 /usr/bin/python3.4
%endif

Name:           python34-%{srcname}
Version:        2.10.6
Release:        2%{?dist}
Summary:        Python client for Redis key-value store
License:        MIT
URL:            https://github.com/andymccurdy/redis-py
Source0:        %pypi_source
BuildArch:      noarch
BuildRequires:  python3-rpm-macros
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools

# Rename from python34u-redis
Provides:       python34u-%{srcname} = %{version}-%{release}
Obsoletes:      python34u-%{srcname} < 2.10.6-2


%description
The Python interface to the Redis key-value store.


%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%files
%license LICENSE
%doc CHANGES README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun Sep 22 2019 Carl George <carl@george.computer> - 2.10.6-2
- Rename to python34-redis
- Switch to EPEL python3 macros

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
