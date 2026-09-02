# If we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# The source directory.
%global source_directory 2.10-stable

%if !0%{?rhel}
# Optional features enabled in this build for Fedora.
%global with_block_driver     1
%global with_glance           1
%global with_ovirt            1
%global with_xen              1

# libguestfs hasn't been built on i686 for a while since there is no
# kernel built for this architecture any longer and libguestfs rather
# fundamentally depends on the kernel.  Therefore we must exclude this
# arch.  Note there is no bug filed for this because we do not ever
# expect that libguestfs or virt-v2v will be available on i686 so
# there is nothing that needs fixing.
ExcludeArch:   %{ix86}

# Version extra string for Fedora.
%global version_extra         fedora=%{fedora},release=%{release}

%else

# Optional features enabled in this build for RHEL.
%global with_block_driver     0
%global with_glance           0
%global with_ovirt            0
%global with_xen              0

# Architectures where virt-v2v is shipped on RHEL:
#
# not on aarch64 because it is not useful there
# not on %%{power64} because of RHBZ#1287826
# not on s390x because it is not useful there
ExclusiveArch: x86_64

# Version extra string for RHEL.
%global version_extra         rhel=%{rhel},release=%{release}

%endif

Name:          virt-v2v
Epoch:         1
Version:       2.10.0
Release:       21%{?dist}
Summary:       Convert a virtual machine to run on KVM

License:       GPL-2.0-or-later AND LGPL-2.0-or-later
URL:           https://github.com/libguestfs/virt-v2v

Source0:       http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:       http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:       libguestfs.keyring
%endif

# Maintainer script which helps with handling patches.
Source3:       copy-patches.sh

# Patches are maintained in the following repository:
# https://github.com/libguestfs/virt-v2v/commits/rhel-10.2

# Patches.
Patch0001:     0001-docs-virt-v2v.pod-Document-Windows-vTPM-and-BitLocke.patch
Patch0002:     0002-input-ssh.ml-Add-debugging-around-remote_file_exists.patch
Patch0003:     0003-input-ssh.ml-Fix-Ssh.remote_file_exists.patch
Patch0004:     0004-Update-common-submodule.patch
Patch0005:     0005-v2v-Enhance-inspection-with-filesystems-information.patch
Patch0006:     0006-inspector-Enhance-virt-v2v-inspector-output-with-fil.patch
Patch0007:     0007-convert-convert_linux.ml-Add-debian-12-UEFI.patch
Patch0008:     0008-input-vcenter-double-uri_encode-dcPath-and-dsName.patch
Patch0009:     0009-lib-Replace-nbdkit-file-cache-none-with-reduce-memor.patch
Patch0010:     0010-convert-convert_linux.ml-Condense-device-regex-handl.patch
Patch0011:     0011-convert-linux-replace-etc-crypttab-dev-sdX-with-UUID.patch
Patch0012:     0012-build-replace-AM_GNU_GETTEXT-with-simpler-LIBINTL-ch.patch
Patch0013:     0013-docs-Drop-references-to-virtio-win-osinfo-usage.patch
Patch0014:     0014-docs-update-virtio-win-exploded-tree-docs.patch
Patch0015:     0015-ocaml-link.sh.in-pass-explicit-guestfs-search-path.patch
Patch0016:     0016-output-introduce-disk_name-helper.patch
Patch0017:     0017-output-Replace-in-VM-names-with-_.patch
Patch0018:     0018-output-sanitize-guest-names-in-metadata-file-paths.patch
Patch0019:     0019-output-sanitize-VM-names-in-libvirt-XML.patch
Patch0020:     0020-Update-common-submodule.patch
Patch0021:     0021-convert-linux-properly-match-etc-crypttab.patch
Patch0022:     0022-Update-common-submodule.patch
Patch0023:     0023-Add-no-fstrim-option-to-disable-fstrim-during-conver.patch
Patch0024:     0024-convert-Stop-using-maxmem-xfs_repair-m-option.patch
Patch0025:     0025-Update-common-submodule.patch
Patch0026:     0026-docs-Show-input-parameters-for-i-input-methods.patch
Patch0027:     0027-docs-i-disk-allows-multiple-disk-images.patch
Patch0028:     0028-i-disk-Allow-nbd-URIs-for-input-disks.patch
Patch0029:     0029-tests-Add-test-for-i-disk-nbd-URI.patch
Patch0030:     0030-common-update-submodule.patch
Patch0031:     0031-common-update-submodule.patch
Patch0032:     0032-RHEL-Fixes-for-libguestfs-winsupport.patch
Patch0033:     0033-RHEL-v2v-Select-correct-qemu-binary-for-o-qemu-mode-.patch
Patch0034:     0034-RHEL-v2v-Disable-the-qemu-boot-oo-qemu-boot-option-R.patch
Patch0035:     0035-RHEL-Fix-list-of-supported-sound-cards-to-match-RHEL.patch
Patch0036:     0036-RHEL-v2v-i-disk-force-VNC-as-display-RHBZ-1372671.patch
Patch0037:     0037-RHEL-point-to-KB-for-supported-v2v-hypervisors-guest.patch
Patch0038:     0038-RHEL-tests-Remove-btrfs-test.patch
Patch0039:     0039-RHEL-Add-warning-about-virt-v2v-in-place-not-being-s.patch
Patch0040:     0040-RHEL-output-output.ml-Remove-reduce-memory-pressure-.patch
Patch0041:     0041-smp-use-cgroup-CPU-limits-for-appliance-SMP.patch
Patch0042:     0042-Update-common-submodule.patch
Patch0043:     0043-convert-Skip-fsck-after-conversion-for-RHEL-7.patch
Patch0044:     0044-convert-linux-Fix-encrypted-ubuntu-24.04.patch
Patch0045:     0045-convert-fix-ubuntu-conversion-regression.patch
Patch0046:     0046-common-update-submodule.patch
Patch0047:     0047-Add-new-collect-option-to-collect-pre-conversion-Win.patch
Patch0048:     0048-inspector-in-place-Add-disk-boot-order-boot-order-to.patch
Patch0049:     0049-common-update-submodule.patch
Patch0050:     0050-mlcustomize-Add-new-selinux-relabel-excludes-flag.patch
Patch0051:     0051-common-update-submodule.patch
Patch0052:     0052-tests-functions.sh.in-Fix-podcheck-to-ignore-new-vir.patch
Patch0053:     0053-Add-selinux-relabel-at-boot-parameter.patch
Patch0054:     0054-Add-it-nfc-mode.patch
Patch0055:     0055-input-input_nfc.ml-Increase-wait-for-nbdkit-timeout-.patch
Patch0056:     0056-lib-nbdkit.mli-Additional-documentation-caveats-for-.patch
Patch0057:     0057-input-input_nfc.ml-Send-dump-plugin-output-to-stderr.patch

BuildRequires: autoconf, automake, libtool
BuildRequires: make
BuildRequires: /usr/bin/pod2man
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IPC::Run3)
BuildRequires: gcc
BuildRequires: ocaml >= 4.08

BuildRequires: libguestfs-devel >= 1:1.58.1-9
BuildRequires: augeas-devel
BuildRequires: bash-completion
%if 0%{?fedora} || 0%{?rhel} >= 11
BuildRequires: bash-completion-devel
%endif
BuildRequires: file
BuildRequires: gettext-devel
BuildRequires: json-c-devel
BuildRequires: libnbd-devel >= 1.24
BuildRequires: libosinfo-devel
BuildRequires: libvirt-daemon-kvm
BuildRequires: libvirt-devel
BuildRequires: libxcrypt-devel
BuildRequires: libxml2-devel
BuildRequires: pcre2-devel
BuildRequires: perl(Sys::Guestfs)
BuildRequires: po4a
BuildRequires: /usr/bin/virsh
BuildRequires: xorriso

BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-libguestfs-devel
BuildRequires: ocaml-libvirt-devel
BuildRequires: ocaml-libnbd-devel
BuildRequires: ocaml-fileutils-devel
BuildRequires: ocaml-gettext-devel

# These are for running our limited test.
BuildRequires: glibc-utils
BuildRequires: %{_bindir}/qemu-nbd
BuildRequires: %{_bindir}/nbdcopy
BuildRequires: %{_bindir}/nbdinfo
BuildRequires: nbdkit-server >= 1.46.1
BuildRequires: nbdkit-file-plugin
BuildRequires: nbdkit-null-plugin
BuildRequires: nbdkit-cow-filter
BuildRequires: mingw-srvany-redistributable >= 1.1-6
%ifarch x86_64
BuildRequires: glibc-static
%endif

%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

Requires:      libguestfs%{?_isa} >= 1:1.58.1-9
Requires:      guestfs-tools >= 1.54

# XFS is the default filesystem in Fedora and RHEL.
Requires:      libguestfs-xfs

%if 0%{?rhel} && ! 0%{?eln}
# For Windows conversions on RHEL.
Requires:      libguestfs-winsupport >= 7.2
%endif

Requires:      curl
Requires:      gawk
Requires:      gzip
Requires:      openssh-clients >= 8.8p1
Requires:      %{_bindir}/openssl
Requires:      unzip
Requires:      %{_bindir}/virsh

# Ensure the UEFI firmware is available, to properly convert
# EFI guests (RHBZ#1429643).
%ifarch x86_64
Requires:      edk2-ovmf
%endif
%ifarch aarch64
Requires:      edk2-aarch64
%endif

%if !%{with_ovirt}
Requires:      /usr/bin/python3
%endif
Requires:      libnbd >= 1.24
Requires:      %{_bindir}/qemu-nbd
Requires:      %{_bindir}/nbdcopy
Requires:      %{_bindir}/nbdinfo
Requires:      nbdkit-server >= 1.46.1
Requires:      nbdkit-curl-plugin
Requires:      nbdkit-file-plugin
Requires:      nbdkit-nbd-plugin
Requires:      nbdkit-null-plugin
%if !%{with_ovirt}
Requires:      nbdkit-python-plugin
%endif
Requires:      nbdkit-ssh-plugin
%ifarch x86_64
Requires:      nbdkit-vddk-plugin
%endif
Requires:      nbdkit-blocksize-filter
Requires:      nbdkit-count-filter
Requires:      nbdkit-cow-filter
Requires:      nbdkit-multi-conn-filter
Requires:      nbdkit-rate-filter
Requires:      nbdkit-retry-filter

# For rhsrvany.exe, used to install firstboot scripts in Windows guests.
Requires:      mingw-srvany-redistributable >= 1.1-6

# On RHEL, virtio-win should be used to install virtio drivers
# and qemu-ga in converted guests.  (RHBZ#1972644)
%if 0%{?rhel}
Recommends:    virtio-win
%endif


%description
Virt-v2v converts a single guest from a foreign hypervisor to run on
KVM.  It can read Linux and Windows guests running on VMware, Xen,
Hyper-V and some other hypervisors, and convert them to KVM managed by
libvirt, OpenStack or several other targets.  It can modify the guest
to make it bootable on KVM and install virtio drivers so it will run
quickly.


%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name} = %{epoch}:%{version}-%{release}


%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%package man-pages-ja
Summary:       Japanese (ja) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.


%package man-pages-uk
Summary:       Ukrainian (uk) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.


%prep
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1

autoreconf -fiv


%build
%configure \
%if %{with_block_driver}
  --enable-block-driver \
%else
  --disable-block-driver \
%endif
%if %{with_glance}
  --enable-glance \
%else
  --disable-glance \
%endif
%if %{with_ovirt}
  --enable-ovirt \
%else
  --disable-ovirt \
%endif
%if %{with_xen}
  --enable-xen \
%else
  --disable-xen \
%endif
  --with-extra="%{version_extra}"

make V=1 %{?_smp_mflags}


%install
%make_install

# Delete libtool crap.
find $RPM_BUILD_ROOT -name '*.la' -delete

%if 0%{?rhel}
# On RHEL move virt-v2v-in-place to libexec since it is not supported,
# and remove the documentation.
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mv $RPM_BUILD_ROOT%{_bindir}/virt-v2v-in-place $RPM_BUILD_ROOT%{_libexecdir}/
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-v2v-in-place.1*
%endif

# Find locale files.
%find_lang %{name}


%check
# Check that the binary runs and the features match those configured.
./run virt-v2v --version
./run virt-v2v --machine-readable | tee machine-readable.out
grep "virt-v2v-2.0" machine-readable.out
grep "input:disk" machine-readable.out
%if %{with_block_driver}
grep "block-driver-option" machine-readable.out
%endif
%if %{with_glance}
grep "output:glance" machine-readable.out
%endif
%if %{with_ovirt}
grep "output:ovirt$" machine-readable.out
grep "output:ovirt-upload" machine-readable.out
grep "output:vdsm" machine-readable.out
%endif

%ifarch x86_64
# Only run the tests with non-debug (ie. non-Rawhide) kernels.
# XXX This tests for any debug kernel installed.
if grep CONFIG_DEBUG_MUTEXES=y /lib/modules/*/config ; then
    echo "Skipping tests because debug kernel is installed"
    exit 0
fi

# Make sure we can see the debug messages (RHBZ#1230160).
export LIBGUESTFS_DEBUG=1
export LIBGUESTFS_TRACE=1

# The built in tests take a very long time to run under TCG (in Koji),
# so just perform a very simple conversion to check things are
# working.
for f in windows.img fedora.img; do
    make -C test-data/phony-guests $f
    if test -s test-data/phony-guests/$f; then
        ./run virt-v2v -v -x -i disk test-data/phony-guests/$f -o null
    fi
done
%endif


%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/virt-v2v
%if !0%{?rhel}
%{_bindir}/virt-v2v-in-place
%else
%{_libexecdir}/virt-v2v-in-place
%endif
%{_bindir}/virt-v2v-inspector
%{_bindir}/virt-v2v-open
%{_mandir}/man1/virt-v2v.1*
%{_mandir}/man1/virt-v2v-hacking.1*
%{_mandir}/man1/virt-v2v-input-vmware.1*
%if %{with_xen}
%{_mandir}/man1/virt-v2v-input-xen.1*
%endif
%if !0%{?rhel}
%{_mandir}/man1/virt-v2v-in-place.1*
%endif
%{_mandir}/man1/virt-v2v-inspector.1*
%{_mandir}/man1/virt-v2v-open.1*
%{_mandir}/man1/virt-v2v-output-local.1*
%{_mandir}/man1/virt-v2v-output-openstack.1*
%if %{with_ovirt}
%{_mandir}/man1/virt-v2v-output-ovirt.1*
%endif
%{_mandir}/man1/virt-v2v-release-notes-1.42.1*
%{_mandir}/man1/virt-v2v-release-notes-2.*.1*
%{_mandir}/man1/virt-v2v-support.1*


%files bash-completion
%license COPYING
%{bash_completions_dir}/virt-v2v


%files man-pages-ja
%license COPYING
%lang(ja) %{_mandir}/ja/man1/*.1*


%files man-pages-uk
%license COPYING
%lang(uk) %{_mandir}/uk/man1/*.1*


%changelog
* Wed Sep 02 2026 Richard W.M. Jones <rjones@redhat.com> - 1:2.10.0-21
- Add -it nfc support
  resolves: RHEL-248249
- Increase timeout
  resolves: RHEL-252892

* Fri Aug 14 2026 Richard W.M. Jones <rjones@redhat.com> - 1:2.10.0-20
- Fix SELinux relabelling of podman rootless containers
  resolves: RHEL-239852
- Add --selinux-relabel-exclude parameter
  resolves: RHEL-239809
- Add --selinux-relabel-at-boot parameter
  resolves: RHEL-RHEL-240649
- Change '::' to 'REM' in Windows batch files for improved reliability
  resolves: RHEL-239810

* Tue Jul 07 2026 Richard W.M. Jones <rjones@redhat.com> - 1:2.10.0-18
- Add <disk> <boot-order>#</boot-order> to XML output
  resolves: RHEL-193138
- Add new --collect option to collect pre-conversion information
  resolves: RHEL-192947
- Retry qemu-ga installer on failure
  resolves: RHEL-193139
- Fix conversions of encrypted Ubuntu guests (second attempt)
  resolves: RHEL-192921
- Skip fsck after conversion for RHEL 7
  resolves: RHEL-192948

* Fri May 22 2026 Richard W.M. Jones <rjones@redhat.com> - 1:2.10.0-17
- Drop 'Fix conversion of encrypted Ubuntu guests' (failed testing)
  related: RHEL-174515
- Fix location of Windows Vista and Windows 2008 Server R1 drivers
  resolves: RHEL-174513

* Tue May 12 2026 Richard W.M. Jones <rjones@redhat.com> - 1:2.10.0-16
- Fix binary LUKS keys
  resolves: RHEL-174520
- Windows firstboot: Add exit code 250 to skip reboots
  Rework documentation for firstboot feature
  resolves: RHEL-174516
- Use cgroups in SMP calculation
  resolves: RHEL-174512

* Thu Apr 23 2026 Richard W.M. Jones <rjones@redhat.com> - 1:2.10.0-13
- Stop using maxmem (xfs_repair -m option)
  resolves: RHEL-169321
- Fix CHS geometry error for Veritas/Sun partitions
  resolves: RHEL-169225

* Fri Apr 03 2026 Richard W.M. Jones <rjones@redhat.com> - 1:2.10.0-11
- Add --no-fstrim option
  resolves: RHEL-164583

* Fri Mar 27 2026 Richard W.M. Jones <rjones@redhat.com> - 1::2.10.0-10
- Create sentinel file after all firstboot scripts have finished running
  resolves: RHEL-161192

* Mon Mar 23 2026 Richard W.M. Jones <rjones@redhat.com> - 1::2.10.0-9
- Requires openssl (for finding thumbprint)
  resolves: RHEL-155204

* Tue Feb 17 2026 Cole Robinson <crobinso@redhat.com> - 1:2.10.0-7
- Attempt 2 to fix sles12sp5 crypttab
  resolves: RHEL-93583

* Thu Feb 12 2026 Cole Robinson <crobinso@redhat.com> - 1:2.10.0-6
- Install blnsvr.exe to \Windows\Drivers\VirtIO
  resolves: RHEL-148423

* Wed Feb 11 2026 Richard W.M. Jones <rjones@redhat.com> - 1:2.10.0-5
- Rebase to virt-v2v 2.10.0
  resolves: RHEL-111241
- Synchronize spec file with Fedora.
- Tighten permissions on windows C:\Program Files\Guestfs
  resolves: RHEL-104352
- Don't output floppy XML with qemu lacks support
  resolves: RHEL-90175
- convert: linux: Ignore /etc/lvm/archive/*.vg files
  resolves: RHEL-113820
- mlcustomize/inject_virtio_win.ml: Use viostor.inf instead of guestor
  resolves: RHEL-112517
- Fix for setting boot order for Linux guests based on grub location
  resolves: RHEL-115989, RHEL-115990
- Remove virt-v2v subscription manager options
  resolves: RHEL-122308
- Handle subdirectories in nbdkit vddk export wildcard
  resolves: RHEL-121728
- Further fixes for nbdkit vddk export wildcard
  resolves: RHEL-122753
- Fix ESP conversion if C:\Windows\Temp has alternate case
  resolves: RHEL-124569
- setfiles runs out of memory in glibc fts_read (doc fix)
  resolves: RHEL-125116
- Use AV and GPO information from inspection instead of open coding
  resolves: RHEL-125956
- Remove reduce-memory-pressure=on as workaround for Dell Powermax 8000
  resolves: RHEL-135617
- Hard depend on libnbd 1.24
  resolves: RHEL-140894
- Add documentation about BitLocker Recovery
  resolves: RHEL-103915
- Fix regression when converting vmx+ssh with snapshots
  resolves: RHEL-102938
- Expose XFS version in virt-v2v-inspector
  resolves: RHEL-144075
- Fix Debian 12 UEFI conversions
  resolves: RHEL-144467
- Fix import when datastore name has characters like '+'
  resolves: RHEL-133729
- Replace /etc/crypttab /dev/sdX with UUID
  resolves: RHEL-93583
- Replace '/' in output name with '_'
  resolves: RHEL-136479

* Thu Aug 21 2025 Richard W.M. Jones <rjones@redhat.com> - 1:2.8.1-9
- Rebase to virt-v2v 2.8.1
  related: RHEL-81735
- Fix virt-v2v -v --install dnf5 error
  resolves: RHEL-83288
- Print blkhash of converted image in virt-v2v debugging output
  resolves: RHEL-85514
- Document dracut network-legacy conversion failure
  resolves: RHEL-55732
- Print nbdcopy command in debug output
  resolves: RHEL-86088
- Remove usage of nbdkit-cacheextents-filter
  resolves: RHEL-88860
- Print better mountpoint stats in debug output
  resolves: RHEL-88862
- Remove several ancient, deprecated options
  resolves: RHEL-88867
- virt-v2v-inspector is failing on snapshots of running VMs
  resolves: RHEL-88544
- Add virt-v2v-open tool
  resolves: RHEL-89993
- Run filesystem check before and after conversion
  resolves: RHEL-91931
- virt-v2v fails to convert XFS guest with dirty filesystem
  resolves: RHEL-95365
- virt-v2v fails to convert guests with e2fsck errors
  resolves: RHEL-97600
- Improve layout of man page
  resolves: RHEL-99745
- Fix xfs_repair out of memory error
  resolves: RHEL-99313
- Remove virt-v2v -io vddk-noextents=true option
  resolves: RHEL-102619
- Add -o kubevirt -oo disk and -oo create options
  resolves: RHEL-101599
- Fix escaping of nbdkit-vddk-plugin export parameter
  resolves: RHEL-102734
- Fix installation of drivers on firstboot with pending reboots
  resolves: RHEL-103356
- Log the version of libnbd / nbdcopy in virt-v2v output
  resolves: RHEL-104018
- Fix SELinux relabelling in Linux split-/usr
  resolves: RHEL-109130
- Set boot order for Linux guests based on grub location
  resolves: RHEL-108991

* Tue Feb 11 2025 Richard W.M. Jones <rjones@redhat.com> - 1:2.7.1-4
- Rebase to virt-v2v 2.7.1
  resolves: RHEL-56814
- Replace Jansson with json-c
  resolves: RHEL-65297
- Find drivers for win2025 guests
  resolves: RHEL-65009
- in-place: Add new -O option to write inspector XML
  resolves: RHEL-70538
- mldrivers/linux_bootloaders.ml: Don't overwrite EFI grub2 wrapper
  resolves: RHEL-78505
- convert: Use yum/apt/... for package removals
  resolves: RHEL-78657

* Wed Aug 28 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.6-2
- convert: windows: Online all virtio disks at first boot
  resolves: RHEL-56318

* Mon Aug 12 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.6-1
- Further fixes for QEMU Guest Agent install & VMware Tools removal
  resolves: RHEL-50563

* Thu Jul 25 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.5-2
- Fix installation of QEMU Guest Agent
  resolves: RHEL-50563

* Thu Jul 11 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.5-1
- New upstream development version 2.5.5
  resolves: RHEL-46869

* Mon Jul 08 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.4-5
- RHEL patches:
  * Select correct qemu binary for -o qemu mode
  * Disable the --qemu-boot / -oo qemu-boot option
  * Fix list of supported sound cards to match RHEL qemu
  * Fixes for libguestfs-winsupport
  * -i disk: force VNC as display
  * point to KB for supported v2v hypervisors/guests
  * Remove -o glance
  * Remove the --in-place option
  * tests: Remove btrfs test
  * Remove --block-driver option
- Remove input from Xen
  resolves: RHEL-37687
- Remove -o rhv, -o rhv-upload and -o vdsm modes
  resolves: RHEL-36712

* Tue Jun 25 2024 Troy Dawson <tdawson@redhat.com> - 1:2.5.4-4
- Bump release for June 2024 mass rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.4-3
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.4-2
- OCaml 5.2.0 for Fedora 41

* Thu Apr 25 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.4-1
- New upstream development version 2.5.4

* Fri Apr 12 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.3-2
- Fix bytecode compilation (RHBZ#2274708)

* Thu Apr 11 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.3-1
- New development branch version 2.5.3
- Unconditionally run autoreconf.

* Mon Mar 25 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.2-2
- Use %%{bash_completions_dir} macro

* Tue Mar 12 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.2-1
- New development branch version 2.5.2

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.5.1-1
- New development branch version 2.5.1

* Thu Jan  4 2024 Richard W.M. Jones <rjones@redhat.com> - 1:2.4.0-1
- New stable branch version 2.4.0

* Tue Dec 19 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.8-1
- New development branch version 2.3.8

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.7-4
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.7-3
- OCaml 5.1.1 rebuild for Fedora 40

* Sat Dec 09 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.7-2
- New development branch version 2.3.7

* Mon Nov 27 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.6-2
- Fix build for libxml2 2.12.1

* Thu Nov 02 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.6-1
- New development branch version 2.3.6

* Fri Oct 20 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1:2.3.5-4
- Use mingw-srvany-redistributable

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.5-3
- OCaml 5.1 rebuild for Fedora 40

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.5-1
- New development branch version 2.3.5

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.4-4
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1:2.3.4-3
- OCaml 5.0.0 rebuild

* Mon Jun 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.4-2
- Migrated to SPDX license
- Fix installation on newer RHEL

* Wed Apr 19 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.4-1
- New development branch version 2.3.4

* Mon Feb 06 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.3-1
- New development branch version 2.3.3

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.2-2
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.2-1
- New development branch version 2.3.2

* Tue Jan 17 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.3.1-1
- New development branch version 2.3.1

* Tue Jan 10 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.2.0-1
- New stable branch version 2.2.0

* Fri Jan 06 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.12-1
- New upstream development version 2.1.12
- Add release notes for future virt-v2v 2.2

* Sat Dec 10 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.11-2
- New upstream development version 2.1.11

* Sat Nov 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.10-1
- New upstream development version 2.1.10
- New tool: virt-v2v-inspector

* Tue Oct 11 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.9-1
- New upstream development version 2.1.9

* Tue Aug 23 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.8-2
- Add BR glibc-static for tests on x86_64.

* Mon Aug 01 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.8-1
- New upstream development version 2.1.8

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.7-1
- New upstream development version 2.1.7

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.6-2
- OCaml 4.14.0 rebuild

* Fri Jun 17 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.6-1
- New upstream development version 2.1.6

* Sat Jun 11 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.5-1
- New upstream development version 2.1.5
- Add Requires python3 / platform-python (RHBZ#2094779)
- Remove nbdkit-readahead-filter as it is no longer used
- Enable the tests

* Thu May 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.4-1
- New upstream development version 2.1.4

* Thu May 12 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.3-1
- New upstream development version 2.1.3

* Tue Apr 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.2-1
- New upstream development version 2.1.2

* Tue Apr 12 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.1.1-1
- New upstream development version 2.1.1

* Mon Apr 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.2-1
- New upstream stable branch version 2.0.2

* Wed Mar 23 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.1-1
- New upstream stable branch version 2.0.1
- Fixes security issue when running virt-v2v as root (RHBZ#2066773).

* Mon Mar 14 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.0-1
- New upstream stable branch version 2.0.0
- New virt-v2v-in-place and release notes man pages.
- Remove the RHEL (downstream) patches which are out of date.
- Don't use absolute symlinks.

* Tue Feb 15 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.99-1
- New upstream development version 1.45.99 (preview of 2.0)
- Requires nbdkit-blocksize-filter.

* Thu Feb 10 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.98-1
- New upstream development version 1.45.98 (preview of 2.0)

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.97-3
- OCaml 4.13.1 rebuild to remove package notes

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.45.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.97-1
- New upstream development version 1.45.97 (preview of 2.0)

* Thu Jan 06 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.96-1
- New upstream development version 1.45.96 (preview of 2.0)

* Sat Dec 18 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.95-1
- New upstream development version 1.45.95 (preview of 2.0)

* Tue Dec 07 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.94-1
- New upstream development version 1.45.94 (preview of 2.0)

* Fri Dec 03 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.93-1
- New upstream development version 1.45.93 (preview of 2.0)

* Thu Dec 02 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.92-1
- New upstream development version 1.45.92 (preview of 2.0)

* Thu Nov 25 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.91-2
- Bump release and rebuild

* Tue Nov 23 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.91-1
- New upstream development version 1.45.91 (preview of 2.0)

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.90-2
- OCaml 4.13.1 build

* Tue Sep 21 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.90-1
- New upstream development version 1.45.90 (preview of 2.0)

* Fri Aug 06 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.3-1
- New upstream development version 1.45.3.
- Rebase RHEL patches.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.45.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.2-1
- New upstream development version 1.45.2.
- Remove --debug-overlays and --print-estimate options.
- Remove -o glance option on RHEL 9 (RHBZ#1977539).
- Remove support for RHEV-APT (RHBZ#1945549).

* Wed Jun 16 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.1-1
- New upstream development version 1.45.1.
- Require virtio-win on RHEL (RHBZ#1972644).
- v2v-test-harness, virt-v2v-copy-to-local have been removed upstream.

* Thu Jun 10 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.44.0-2
- nbdkit-vddk-plugin dep only exists on x86-64.

* Fri Apr 30 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.44.0-1
- New upstream stable branch version 1.44.0.

* Wed Apr 14 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.5-1
- New upstream version 1.43.5.

* Thu Apr 01 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.4-5
- Add upstream patch to depend on xorriso.
- Change libguestfs-tools-c -> guestfs-tools.

* Tue Mar 30 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.4-3
- Add downstream (RHEL-only) patches (RHBZ#1931724).

* Mon Mar  8 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.4-2
- Bump and rebuild for ocaml-gettext update.

* Wed Mar  3 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.4-1
- New upstream version 1.43.4.

* Tue Mar  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.3-4
- OCaml 4.12.0 build

* Tue Mar  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.3-3
- Add fix for OCaml 4.12.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.43.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.3-1
- New upstream version 1.43.3.

* Thu Dec 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.2-3
- Drop obsolete virt-v2v-copy-to-local tool for Fedora 34 and RHEL 9.

* Wed Dec 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.2-2
- Unify Fedora and RHEL spec files.

* Tue Dec 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.2-1
- New upstream version 1.43.2.

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.1-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.1-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.43.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Richard W.M. Jones <rjones@redhat.com> - 1.43.1-1
- New development branch 1.43.

* Wed May 06 2020 Richard W.M. Jones <rjones@redhat.com> - 1.42.0-4
- Re-add Epoch.  Forgotten when we split this package from libguestfs.

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.42.0-2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

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
