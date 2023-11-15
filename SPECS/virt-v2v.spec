# If we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# If there are patches which touch autotools files, set this to 1.
%global patches_touch_autotools 1

# The source directory.
%global source_directory 1.42-stable

Name:          virt-v2v
Epoch:         1
Version:       1.42.0
Release:       22%{?dist}
Summary:       Convert a virtual machine to run on KVM

License:       GPLv2+
URL:           https://github.com/libguestfs/virt-v2v

Source0:       http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:       http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:       libguestfs.keyring
%endif

# Architectures where virt-v2v is shipped.
#
# not on aarch64 because it is not useful there
# not on %%{power64} because of RHBZ#1287826
# not on s390x because it is not useful there
ExclusiveArch: x86_64

# RHEL 8 git repository is:
# https://github.com/libguestfs/virt-v2v/tree/rhel-8.6.0
# Use 'copy-patches.sh' to copy the patches from the git repo
# to the current directory.

# Patches.
Patch0001:     0001-libvirt-make-use-of-libvirt-s-default-auth-handler-R.patch
Patch0002:     0002-i-libvirt-print-URI-without-connecting-RHBZ-1839917.patch
Patch0003:     0003-vCenter-fix-parsing-of-HTTP-status-string-RHBZ-18373.patch
Patch0004:     0004-v2v-o-libvirt-Remove-cache-none-RHBZ-1837453.patch
Patch0005:     0005-v2v-Remove-extraneous-when-setting-bandwidth-RHBZ-18.patch
Patch0006:     0006-v2v-it-vddk-Don-t-use-nbdkit-readahead-filter-with-V.patch
Patch0007:     0007-v2v-nbdkit-Handle-password-parameter-in-common_creat.patch
Patch0008:     0008-v2v-nbdkit-Don-t-use-password-parameter-RHBZ-1842440.patch
Patch0009:     0009-libosinfo-declare-autocleanup-funcs-with-libosinfo-1.patch
Patch0010:     0010-v2v-Use-common-documentation-for-keys-from-stdin.patch
Patch0011:     0011-docs-Multiple-keys-must-be-supplied-one-per-line-RHB.patch
Patch0012:     0012-v2v-Check-that-mac-ip-parameters-are-sensible-RHBZ-1.patch
Patch0013:     0013-libvirt-read-password-file-outside-libvirt-auth-call.patch
Patch0014:     0014-RHEL-8-v2v-Select-correct-qemu-binary-for-o-qemu-mod.patch
Patch0015:     0015-RHEL-8-v2v-Disable-the-qemu-boot-option-RHBZ-1147313.patch
Patch0016:     0016-RHEL-8-Fix-list-of-supported-sound-cards-to-match-RH.patch
Patch0017:     0017-RHEL-8-Fix-tests-for-libguestfs-winsupport.patch
Patch0018:     0018-RHEL-8-v2v-Disable-the-virt-v2v-in-place-option.patch
Patch0019:     0019-RHEL-8-v2v-i-disk-force-VNC-as-display-RHBZ-1372671.patch
Patch0020:     0020-RHEL-8-v2v-do-not-mention-SUSE-Xen-hosts-RHBZ-143020.patch
Patch0021:     0021-RHEL-8-v2v-rhv-upload-Remove-restriction-on-oa-spars.patch
Patch0022:     0022-RHEL-8-use-platform-python.patch
Patch0023:     0023-RHEL-8-point-to-KB-for-supported-v2v-hypervisors-gue.patch
Patch0024:     0024-v2v-Allow-large-temporary-directory-to-be-set-on-a-g.patch
Patch0025:     0025-v2v-o-openstack-Allow-guests-to-be-converted-to-UEFI.patch
Patch0026:     0026-v2v-Fix-spelling-mistake-in-uninstall-function-name.patch
Patch0027:     0027-v2v-windows-Refactor-uninstallation_commands-functio.patch
Patch0028:     0028-v2v-Replace-broken-VMware-Tools-uninstall-command-ms.patch
Patch0029:     0029-Update-common-submodule-to-latest-upstream.patch
Patch0030:     0030-v2v-rhv-upload-plugin-Defer-imageio-connection.patch
Patch0031:     0031-v2v-windows-Fix-schtasks-SD-parameter.patch
Patch0032:     0032-v2v-Turn-pnp_wait.exe-warning-into-a-debug-message.patch
Patch0033:     0033-docs-UEFI-guest-conversion-to-o-openstack-is-support.patch
Patch0034:     0034-docs-o-openstack-Clarify-name-of-file-containing-Ope.patch
Patch0035:     0035-v2v-Allow-output-to-block-devices-RHBZ-1868690.patch
Patch0036:     0036-v2v-Disable-readahead-for-VMware-curl-sources-too-RH.patch
Patch0037:     0037-docs-Document-how-to-remove-Out-of-HTTP-sessions-lim.patch
Patch0038:     0038-v2v-Increase-required-free-space-in-Windows-to-100-M.patch
Patch0039:     0039-v2v-windows-Allow-qxldod.inf-as-synonym-for-qxl.inf.patch
Patch0040:     0040-RHEL-8-docs-Fix-version-of-virt-v2v-which-added-UEFI.patch
Patch0041:     0041-v2v-Increase-Linux-minimum-root-filesystem-to-100-MB.patch
Patch0042:     0042-v2v-rhv-upload-plugin-Fix-waiting-for-finalize.patch
Patch0043:     0043-v2v-windows-Do-not-fix-NTFS-heads-in-Windows-Vista-a.patch
Patch0044:     0044-v2v-vcenter-Implement-cookie-scripts.patch
Patch0045:     0045-convert-convert_windows.ml-Handle-date-formats-with-.patch
Patch0046:     0046-v2v-Force-format-of-input-to-be-specified.patch
Patch0047:     0047-v2v-Cope-with-libvirt-vpx-esx-driver-which-does-not-.patch
Patch0048:     0048-o-rhv-upload-wait-for-VM-creation-task.patch
Patch0049:     0049-tests-Add-test-of-i-ova-from-a-directory.patch
Patch0050:     0050-v2v-i-ova-Fix-parsing-if-OVA-directory-name-has-a-tr.patch
Patch0051:     0051-convert-If-listing-RPM-applications-fails-rebuild-DB.patch
Patch0052:     0052-update-common-submodule-for-CVE-2022-2211-fix.patch
Patch0053:     0053-RHEL-8-If-setfiles-fails-fall-back-to-autorelabel.patch

# Use git for patch management.
BuildRequires: git

%if 0%{patches_touch_autotools}
BuildRequires: autoconf, automake, libtool
%endif

# RHSRVANY and RHEV-APT, used for Windows virt-v2v conversions.
# RHSRVANY is built from source under Fedora from
# mingw32-srvany-1.0-15.20150115gitfd659e77.fc23.noarch
# RHEV-APT is taken from the RHEV Tools CD
# See https://bugzilla.redhat.com/show_bug.cgi?id=1186850
Source94:      rhsrvany-fd659e77cdd9da484fdc9dcbe0605c62ec26fa30.tar.gz
Source95:      SOURCES
Source96:      rhsrvany.exe
Source97:      RHEV-Application-Provisioning-Tool.exe_4.43-5

Source99:      copy-patches.sh

BuildRequires: /usr/bin/pod2man
BuildRequires: gcc
BuildRequires: ocaml >= 4.01
BuildRequires: libguestfs-devel >= 1:1.42

BuildRequires: augeas-devel
BuildRequires: bash-completion
BuildRequires: file-devel
BuildRequires: gettext-devel
BuildRequires: jansson-devel
BuildRequires: libosinfo-devel
BuildRequires: libvirt-devel
BuildRequires: libvirt-daemon-kvm
BuildRequires: libxml2-devel
BuildRequires: pcre-devel
BuildRequires: perl(Sys::Guestfs)
BuildRequires: po4a
BuildRequires: /usr/bin/virsh

BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-libguestfs-devel
BuildRequires: ocaml-fileutils-devel
BuildRequires: ocaml-gettext-devel

BuildRequires: nbdkit-python-plugin

%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

Requires:      libguestfs%{?_isa} >= 1:1.42
Requires:      libguestfs-tools-c >= 1:1.42

# For Windows conversions.
Requires:      libguestfs-winsupport >= 7.2

Requires:      gawk
Requires:      gzip
Requires:      unzip
Requires:      curl

# Ensure the UEFI firmware is available, to properly convert
# EFI guests (RHBZ#1429643).
%ifarch x86_64
Requires:      edk2-ovmf
%endif
%ifarch aarch64
Requires:      edk2-aarch64
%endif

# Needed for -it vddk, and -o rhv-upload.
Requires:      nbdkit
Requires:      nbdkit-curl-plugin
Requires:      nbdkit-python-plugin
Requires:      nbdkit-ssh-plugin
Requires:      nbdkit-vddk-plugin
Requires:      platform-python


%description
Virt-v2v converts a single guest from a foreign hypervisor to run on
KVM.  It can read Linux and Windows guests running on VMware, Xen,
Hyper-V and some other hypervisors, and convert them to KVM managed by
libvirt, OpenStack, oVirt, Red Hat Virtualisation (RHV) or several
other targets.  It can modify the guest to make it bootable on KVM and
install virtio drivers so it will run quickly.


%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name} = %{epoch}:%{version}-%{release}

# The bash completion for virt-v2v were shipped with the others of libguestfs:
Obsoletes: libguestfs-bash-completion < 1:1.42.0


%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%package man-pages-ja
Summary:       Japanese (ja) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

# The man pages for virt-v2v were shipped with the others of libguestfs:
Obsoletes: libguestfs-man-pages-ja < 1:1.42.0

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.


%package man-pages-uk
Summary:       Ukrainian (uk) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

# The man pages for virt-v2v were shipped with the others of libguestfs:
Obsoletes: libguestfs-man-pages-uk < 1:1.42.0

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.


%prep
%if 0%{verify_tarball_signature}
tmphome="$(mktemp -d)"
gpgv2 --homedir "$tmphome" --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%endif
%setup -q

# Use git to manage patches.
# http://rwmj.wordpress.com/2011/08/09/nice-rpm-git-patch-management-trick/
git init
git config user.email "libguestfs@redhat.com"
git config user.name "libguestfs"
git add .
git commit -a -q -m "%{version} baseline"
git am %{patches}

%if 0%{patches_touch_autotools}
autoreconf -fi
%endif


%build
%configure \
  --with-extra="rhel=%{rhel},release=%{release}"

make V=1 %{?_smp_mflags}


%install
%make_install

# Virt-tools data directory.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/virt-tools
cp %{SOURCE96} $RPM_BUILD_ROOT%{_datadir}/virt-tools/rhsrvany.exe
cp %{SOURCE97} $RPM_BUILD_ROOT%{_datadir}/virt-tools/rhev-apt.exe

# Delete the v2v test harness.
rm -r $RPM_BUILD_ROOT%{_libdir}/ocaml/v2v_test_harness
rm -r $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/dllv2v_test_harness*
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-v2v-test-harness.1*

# Find locale files.
%find_lang %{name}


%check
# All tests fail at the moment because of bugs in libvirt blockdev.
# # Tests fail on both armv7 and ppc64le in Fedora 31 because the kernel
# # cannot boot on qemu.
# %ifnarch %{arm} ppc64le

# # On x86_64 this single test fails with: "virt-v2v: warning: the
# # target hypervisor does not support a x86_64 KVM guest".  Missing
# # BuildRequires?
# %ifarch x86_64
# truncate -s 0 tests/test-v2v-o-libvirt.sh
# %endif

# # This test fails in mock.
# truncate -s 0 tests/test-v2v-oa-option.sh

# # Make sure we can see the debug messages (RHBZ#1230160).
# export LIBGUESTFS_DEBUG=1
# export LIBGUESTFS_TRACE=1

# make %{?_smp_mflags} check || {
#     cat tests/test-suite.log
#     exit 1
#   }

# %endif


%files -f %{name}.lang
%doc COPYING README
%{_bindir}/virt-v2v
%{_bindir}/virt-v2v-copy-to-local
%{_mandir}/man1/virt-v2v.1*
%{_mandir}/man1/virt-v2v-copy-to-local.1*
%{_mandir}/man1/virt-v2v-hacking.1*
%{_mandir}/man1/virt-v2v-input-vmware.1*
%{_mandir}/man1/virt-v2v-input-xen.1*
%{_mandir}/man1/virt-v2v-output-local.1*
%{_mandir}/man1/virt-v2v-output-openstack.1*
%{_mandir}/man1/virt-v2v-output-rhv.1*
%{_mandir}/man1/virt-v2v-release-notes-1.42.1*
%{_mandir}/man1/virt-v2v-support.1*
%{_datadir}/virt-tools


%files bash-completion
%doc COPYING
%{_datadir}/bash-completion/completions/virt-v2v
%{_datadir}/bash-completion/completions/virt-v2v-copy-to-local


%files man-pages-ja
%doc COPYING
%lang(ja) %{_mandir}/ja/man1/*.1*


%files man-pages-uk
%doc COPYING
%lang(uk) %{_mandir}/uk/man1/*.1*


%changelog
* Mon Apr 03 2023 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-22
- RHEL 8: If setfiles fails fall back to autorelabel
  resolves: rhbz#XXX
- Reapply patches since we are using git format-patch --submodule=diff

* Tue Jul 05 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-21
- Fix assertion failure when parsing OVA dir with trailing slash
  resolves: rhbz#2028823
- For -o rhv-upload wait for VM creation task
  resolves: rhbz#1985827
- If listing RPM applications fails, rebuild DB and retry (2089623)
- Fix CVE-2022-2211 Denial of Service in --key parameter
  resolves: rhbz#2102720

* Wed Nov 24 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-18
- Additional fix for backing file specified without backing format
  related: rhbz#2025769

* Tue Nov 23 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-17
- Correct regexps used to fix schtasks command
- Fix backing file specified without backing format
  resolves: rhbz#2023279, rhbz#2025769

* Fri Oct 29 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-16
- Implement cookie scripts for more reliable vCenter/HTTPS transfers
  resolves: rhbz#2018173

* Wed Aug 18 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-15
- v2v: windows: Do not fix NTFS heads in Windows Vista and later
  resolves: rhbz#1995000

* Fri Jul 16 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-14
- v2v: rhv-upload-plugin: Fix waiting for finalize
  resolves: rhbz#1976024

* Wed Jun 30 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-13
- docs: Fix version of virt-v2v which added UEFI for OpenStack
  related: rhbz#1872100
- v2v: Increase Linux minimum root filesystem to 100 MB
  resolves: rhbz#1764569

* Tue May 11 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-12
- v2v: Fix conversion of BitLocker guests
  resolves: rhbz#1959051

* Tue Apr 27 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-11
- v2v: windows: Allow qxldod.inf as synonym for qxl.inf
  resolves: rhbz#1926102
- v2v: Increase required free space in Windows to 100 MB
  resolves: rhbz#1949147
- docs: Document how to remove "Out of HTTP sessions" limit
- v2v: Disable readahead for VMware curl sources too
  resolves: rhbz#1848862
- v2v: Allow output to block devices
  resolves: rhbz#1868690
- docs: -o openstack: Clarify name of file containing OpenStack auth
  resolves: rhbz#1871754
- docs: UEFI guest conversion to -o openstack is supported
  resolves: rhbz#1872100
- v2v: Turn pnp_wait.exe warning into a debug message
  resolves: rhbz#1903960
- v2v: windows: Fix schtasks /SD parameter
  resolves: rhbz#1895323

* Thu Jan 21 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-9
- v2v: rhv-upload-plugin: Defer imageio connection
  resolves: rhbz#1911568

* Tue Jan 19 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-8
- Replace broken VMware Tools uninstall command msiexec /i with /x.
  resolves: rhbz#1917760

* Tue Jan 12 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.42.0-7
- Tell virt-v2v where overlay files must be placed
- Allow conversion to UEFI openstack
  resolves: rhbz#1820282 rhbz#1872094

* Tue Sep 01 2020 Pino Toscano <ptoscano@redhat.com> - 1:1.42.0-6
- Improve the documentation of --keys-from-stdin
  resolves: rhbz#1858765
- Check that --mac :ip: parameters are sensible
  resolves: rhbz#1858775
- -i libvirt: read password file outside libvirt auth callback
  resolves: rhbz#1869454

* Wed Jun 24 2020 Pino Toscano <ptoscano@redhat.com> - 1:1.42.0-5
- Ship a newer version of rhev-apt.exe
  resolves: rhbz#1850000
- Ship the rhsrvany sources with a note for them, as requested by
  Red Hat Legal.
- -i libvirt: ask for the password ourselves instead of letting nbdkit
  ask for it (and potentially time out)
  related: rhbz#1838425
- Fix build with libosinfo >= 1.8.0
  resolves: rhbz#1850423

* Thu May 28 2020 Pino Toscano <ptoscano@redhat.com> - 1:1.42.0-4
- -i libvirt: ask again for the password when -ip is not specified
  resolves: rhbz#1838425
- -i libvirt: print URI without connecting
  resolves: rhbz#1839917
- Handle HTTP/2 replies from vCenter
  resolves: rhbz#1840126
- -o libvirt: remove cache=none from disks
  resolves: rhbz#1837453
- Fix parameters for the nbdkit rate filter
  resolves: rhbz#1841096
- -it vddk: do not use the nbdkit readahead filter with VDDK
  resolves: rhbz#1832805

* Wed May 06 2020 Pino Toscano <ptoscano@redhat.com> - 1:1.42.0-3
- Actually fix epoch dependencies.
- Fix virt-v2v-man-pages-uk migration from libguestfs-man-pages-uk.

* Wed May 06 2020 Pino Toscano <ptoscano@redhat.com> - 1:1.42.0-2
- Bump the libguestfs requirement to 1.42.0.
- Bump the epoch to 1 to match the version virt-v2v had when built from
  the libguestfs source.

* Thu Apr 16 2020 Richard W.M. Jones <rjones@redhat.com> - 1.42.0-1
- New upstream stable version 1.42.0.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-11
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-10
- OCaml 4.10.0 final.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-8
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-7
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-6
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-5
- OCaml 4.10.0+beta1 rebuild.
- Use nbdkit-python-plugin (now all Python 3 in Rawhide).

* Wed Nov 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-4
- Use license instead of doc for COPYING file.
- Include license in all subpackages.
- Use gpgverify macro.
- Don't own bash-completion directory because we Require the
  bash-completion package which owns it already.

* Tue Nov 26 2019 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-2
- Fix permissions on .sig file.
- Disable -oa preallocated test since it fails in reviewers mock environment.

* Fri Nov 15 2019 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-1
- Initial release of separate virt-v2v program, was part of libguestfs.
