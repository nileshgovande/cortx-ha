Name: <RPM_NAME>
Version: %{version}
Release: %{dist}
Summary: HA Tools
License: Seagate Proprietary
URL: http://gitlab.mero.colo.seagate.com/eos/cortx-ha
Source0: <RPM_NAME>-%{version}.tar.gz
#TODO: Dependency on Hare rpm
%define debug_package %{nil}

%description
HA Tools

%prep
%setup -n cortx
# Nothing to do here

%build

%install
mkdir -p ${RPM_BUILD_ROOT}<HA_PATH>
cp -rp . ${RPM_BUILD_ROOT}<HA_PATH>
exit 0

%post
HA_DIR=<HA_PATH>/ha
RES_AGENT="/usr/lib/ocf/resource.d/seagate"
mkdir -p ${RES_AGENT} $HA_DIR/bin /var/seagate/cortx/ha/

# Move binary file
ln -sf $HA_DIR/lib/hw_comp_ra ${RES_AGENT}/hw_comp_ra
ln -sf $HA_DIR/lib/hw_comp_ra $HA_DIR/bin/hw_comp_ra
exit 0

%preun
exit 0

%postun
[ $1 -eq 1 ] && exit 0
HA_DIR=<HA_PATH>/ha
RES_AGENT="/usr/lib/ocf/resource.d/seagate"
rm -f $HA_DIR/bin/hw_comp_ra 2> /dev/null;
rm -f ${RES_AGENT}/hw_comp_ra 2> /dev/null;
exit 0

%clean

%files
# TODO - Verify permissions, user and groups for directory.
%defattr(-, root, root, -)
<HA_PATH>/*

%changelog
* Mon Jul 29 2019 Ajay Paratmandali <ajay.paratmandali@seagate.com> - 1.0.0
- Initial spec file