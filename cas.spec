%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: cas
Summary: Tool to analyze and configure core file environment
Version: 0.15
Release: 1%{?dist}.1
Source0: https://fedorahosted.org/releases/c/a/cas/%{name}-%{version}.tar.gz
License: GPLv3+
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://fedorahosted.org/cas
BuildRequires: python-devel
%if 0%{?rhel}
Requires: python-sqlite crash python-paramiko
%else
Requires: crash python-paramiko
%endif

%description
CAS provides a user the ability to configure an environment for core analysis
quickly. All the hassles of matching kernel versions and machine architecture
types to core dumps are automatically detected and processed.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf ${RPM_BUILD_ROOT}
%{__python} setup.py install -O1 --skip-build --root ${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/cas.conf
%{_bindir}/cas
%{_bindir}/cas-admin
%{python_sitelib}/*
%{_mandir}/man1/cas.1.gz
%{_mandir}/man1/cas-admin.1.gz
%dir %{_var}/lib/cas/snippets/
%defattr(755,root,root)
%config(noreplace) %{_var}/lib/cas/snippets/*
%doc AUTHORS LICENSE README PKG-INFO doc/*

%changelog
* Thu Oct 15 2009 Adam Stokes <ajs at redhat dot com> - 0.15-1
- Require paramiko for all remote executions
- Rip out func code
- Documentation update to include ssh setup

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 5 2009 Adam Stokes <ajs at redhat dot com> - 0.14-8
- support for purging old data
- documentation updated to reflect updated workflow and describe
  new features.

* Fri Apr 24 2009 Adam Stokes <ajs at redhat dot com> - 0.14-2
- Finalizing sqlite implementation
- added AUTHORS

* Thu Apr 2 2009 Scott Dodson <sdodson at sdodson dot com > - 0.14-1
- Spec file changes to handle the snippets directory
- Snippets support to replace hardcoding crash input cmds

* Wed Feb 11 2009 Adam Stokes <ajs at redhat dot com> - 0.13-120
- added proper documentation

* Wed Jan 7 2009 Adam Stokes <ajs at redhat dot com> - 0.13-116
- support for extracting kernel modules
- support for analyzing x86 cores on x86_64 system
- consistent macro usage in spec

* Mon Dec 29 2008 Adam Stokes <ajs at redhat dot com> - 0.13-114
- changed license to gplv3 or later
- removed source requirements as these are handled by python manifest
- removed python requirement
- updated description

* Fri Dec 19 2008 Adam Stokes <ajs at redhat dot com> - 0.13-113
- rpmlint verified
- manually set version/release in spec
- license tag fix
- added full path to upstream source release

* Mon Dec 15 2008 Adam Stokes <ajs at redhat dot com> - 0.13-94
- no replace on config file
- cas now processes locally and remotely via func

* Wed Aug 20 2008 Adam Stokes <ajs at redhat dot com> - 0.13
- Updated build and spec

* Mon Feb 10 2008 Scott Dodson <sdodson at redhat dot com> - 0.11
- Minor changes to permissions

* Mon Dec 10 2007 Adam Stokes <astokes at redhat dot com> - 0.9.1
- splitting off grabcore to be a download/extract only service
- core of the work to be done specifically by their intended
  modules

* Fri Dec 7 2007 Adam Stokes <astokes at redhat dot com> - 0.9
- release bump
- decompression module added

* Tue Nov 13 2007 Adam Stokes <astokes at redhat dot com> - 0.8
- threading added
- better exception handling
- bug fixes
- added initscripts, service capabilities

* Mon Oct 22 2007 Adam Stokes <astokes at redhat dot com> - 0.1
- initial build
