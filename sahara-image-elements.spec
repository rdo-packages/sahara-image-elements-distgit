%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           sahara-image-elements
Epoch:          1
Version:        6.0.3
Release:        1%{?dist}
Summary:        Image creation tools for Openstack Sahara

License:        ASL 2.0
URL:            https://launchpad.net/sahara
Source0:        https://tarballs.openstack.org/sahara-image-elements/sahara-image-elements-%{version}%{?milestone}.tar.gz
BuildArch:      noarch

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr >= 0.5.19

Requires: dib-utils
Requires: diskimage-builder >= 0.1.34-21
Requires: rsync
Requires: wget
Requires: qemu-kvm
Requires: qemu-img
Requires: kpartx
Requires: git

%description
Sahara-image-elements provides the ability to create the images necessary to generate data processing clusters
in Sahara.

%prep
%setup -q -n sahara-image-elements-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc AUTHORS LICENSE ChangeLog
%{_bindir}/sahara-image-create
%{_bindir}/diskimage-create.sh
%{_datadir}/sahara-elements
%{python2_sitelib}/sahara_image_elements-%{upstream_version}-py?.?.egg-info

%changelog
* Mon Feb 19 2018 RDO <dev@lists.rdoproject.org> 1:6.0.3-1
- Update to 6.0.3

* Sun Aug 27 2017 rdo-trunk <javier.pena@redhat.com> 1:6.0.2-1
- Update to 6.0.2

* Wed Jul 05 2017 rdo-trunk <javier.pena@redhat.com> 1:6.0.1-1
- Update to 6.0.1

* Wed Feb 22 2017 Alfredo Moralejo <amoralej@redhat.com> 1:6.0.0-1
- Update to 6.0.0

* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 1:6.0.0-0.1.0rc1
- Update to 6.0.0.0rc1

