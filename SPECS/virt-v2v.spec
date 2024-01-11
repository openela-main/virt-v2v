%undefine _package_note_flags
# If we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# If there are patches which touch autotools files, set this to 1.
%if !0%{?rhel}
%global patches_touch_autotools %{nil}
%else
# On RHEL the downstream patches always touch autotools files.
%global patches_touch_autotools 1
%endif

# The source directory.
%global source_directory 2.2-stable

Name:          virt-v2v
Epoch:         1
Version:       2.2.0
Release:       6%{?dist}
Summary:       Convert a virtual machine to run on KVM

License:       GPLv2+
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
# https://github.com/libguestfs/virt-v2v/commits/rhel-9.2

# Patches.
Patch0001:     0001-test-v2v-fedora-btrfs-conversion-spell-out-btrfs-fea.patch
Patch0002:     0002-test-v2v-i-ova-spell-out-ntfs-feature-group-dependen.patch
Patch0003:     0003-Translated-using-Weblate-Finnish.patch
Patch0004:     0004-Translated-using-Weblate-Georgian.patch
Patch0005:     0005-Update-translation-files.patch
Patch0006:     0006-Translated-using-Weblate-Ukrainian.patch
Patch0007:     0007-convert-windows-Remove-extraneous-blank-lines-in-sou.patch
Patch0008:     0008-convert-windows-Document-what-copy_qemu_ga-function-.patch
Patch0009:     0009-convert-windows-Remove-unused-open-Utils.patch
Patch0010:     0010-o-kubevirt-Fix-mistake-in-error-message.patch
Patch0011:     0011-o-kubevirt-Move-cpu-element-under-domain.patch
Patch0012:     0012-o-kubevirt-Error-on-invalid-output-guest-names.patch
Patch0013:     0013-Split-long-lines-in-messages.patch
Patch0014:     0014-o-kubevirt-Implement-oo-compressed-for-qcow2-files.patch
Patch0015:     0015-v2v-Remove-use-of-anchored.patch
Patch0016:     0016-o-kubevirt-Replace-PCRE-anchored-with.patch
Patch0017:     0017-o-libvirt-Add-correct-xmlns-libosinfo-for-Rocky-Linu.patch
Patch0018:     0018-convert-linux-Require-host-cpu-for-all-RHEL-alike-9.patch
Patch0019:     0019-detect_kernels-tighten-try-scope.patch
Patch0020:     0020-detect_kernels-deal-with-RHEL-s-kernel-core-kernel-m.patch
Patch0021:     0021-RHEL-v2v-Select-correct-qemu-binary-for-o-qemu-mode-.patch
Patch0022:     0022-RHEL-v2v-Disable-the-qemu-boot-oo-qemu-boot-option-R.patch
Patch0023:     0023-RHEL-Fix-list-of-supported-sound-cards-to-match-RHEL.patch
Patch0024:     0024-RHEL-Fixes-for-libguestfs-winsupport.patch
Patch0025:     0025-RHEL-v2v-i-disk-force-VNC-as-display-RHBZ-1372671.patch
Patch0026:     0026-RHEL-v2v-do-not-mention-SUSE-Xen-hosts-RHBZ-1430203.patch
Patch0027:     0027-RHEL-point-to-KB-for-supported-v2v-hypervisors-guest.patch
Patch0028:     0028-RHEL-Disable-o-glance.patch
Patch0029:     0029-RHEL-Remove-the-in-place-option.patch
Patch0030:     0030-RHEL-9-oo-compressed-Remove-nbdcopy-version-check-an.patch
Patch0031:     0031-RHEL-9-tests-Remove-btrfs-test.patch

%if !0%{?rhel}
# libguestfs hasn't been built on i686 for a while since there is no
# kernel built for this architecture any longer and libguestfs rather
# fundamentally depends on the kernel.  Therefore we must exclude this
# arch.  Note there is no bug filed for this because we do not ever
# expect that libguestfs or virt-v2v will be available on i686 so
# there is nothing that needs fixing.
ExcludeArch:   %{ix86}
%else
# Architectures where virt-v2v is shipped on RHEL:
#
# not on aarch64 because it is not useful there
# not on %%{power64} because of RHBZ#1287826
# not on s390x because it is not useful there
ExclusiveArch: x86_64
%endif

%if 0%{patches_touch_autotools}
BuildRequires: autoconf, automake, libtool
%endif

BuildRequires: make
BuildRequires: /usr/bin/pod2man
BuildRequires: gcc
BuildRequires: ocaml >= 4.04

BuildRequires: libguestfs-devel >= 1:1.44
BuildRequires: augeas-devel
BuildRequires: bash-completion
BuildRequires: file-devel
BuildRequires: gettext-devel
BuildRequires: jansson-devel
BuildRequires: libnbd-devel
BuildRequires: libosinfo-devel
BuildRequires: libvirt-daemon-kvm
BuildRequires: libvirt-devel
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
%if !0%{?rhel}
BuildRequires: ocaml-ounit-devel
%endif

# These are for running our limited test.
BuildRequires: %{_bindir}/qemu-nbd
BuildRequires: %{_bindir}/nbdcopy
BuildRequires: %{_bindir}/nbdinfo
BuildRequires: nbdkit-file-plugin
BuildRequires: nbdkit-null-plugin
BuildRequires: nbdkit-python-plugin
BuildRequires: nbdkit-cow-filter >= 1.28.3-1.el9
%ifarch x86_64
BuildRequires: glibc-static
%endif

%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

Requires:      libguestfs%{?_isa} >= 1:1.48.4-4.el9
Requires:      guestfs-tools >= 1.42

# XFS is the default filesystem in Fedora and RHEL.
Requires:      libguestfs-xfs

%if 0%{?rhel}
# For Windows conversions on RHEL.
Requires:      libguestfs-winsupport >= 7.2
%endif

Requires:      gawk
Requires:      gzip
Requires:      unzip
Requires:      curl
Requires:      openssh-clients >= 8.7p1
Requires:      %{_bindir}/virsh

# Ensure the UEFI firmware is available, to properly convert
# EFI guests (RHBZ#1429643).
%ifarch x86_64
Requires:      edk2-ovmf
%endif
%ifarch aarch64
Requires:      edk2-aarch64
%endif

%if !0%{?rhel}
Requires:      python3
%else
Requires:      platform-python
%endif
Requires:      libnbd >= 1.12.4-2.el9
Requires:      %{_bindir}/qemu-nbd
Requires:      %{_bindir}/nbdcopy
Requires:      %{_bindir}/nbdinfo
Requires:      nbdkit-server >= 1.28.3-1.el9
Requires:      nbdkit-curl-plugin
Requires:      nbdkit-file-plugin
Requires:      nbdkit-nbd-plugin
Requires:      nbdkit-null-plugin
Requires:      nbdkit-python-plugin
Requires:      nbdkit-ssh-plugin
%ifarch x86_64
Requires:      nbdkit-vddk-plugin
%endif
Requires:      nbdkit-blocksize-filter
Requires:      nbdkit-cacheextents-filter
Requires:      nbdkit-cow-filter >= 1.28.3-1.el9
Requires:      nbdkit-multi-conn-filter
Requires:      nbdkit-rate-filter
Requires:      nbdkit-retry-filter

# For rhsrvany.exe, used to install firstboot scripts in Windows guests.
Requires:      mingw32-srvany >= 1.0-13

# On RHEL, virtio-win should be used to install virtio drivers
# and qemu-ga in converted guests.  (RHBZ#1972644)
%if 0%{?rhel}
Recommends:    virtio-win
%endif


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

%if 0%{patches_touch_autotools}
autoreconf -i
%endif


%build
%configure \
%if !0%{?rhel}
  --with-extra="fedora=%{fedora},release=%{release}" \
%else
  --with-extra="rhel=%{rhel},release=%{release}" \
%endif

make V=1 %{?_smp_mflags}


%install
%make_install

# Delete libtool crap.
find $RPM_BUILD_ROOT -name '*.la' -delete

# Virt-tools data directory.  This contains symlinks to rhsrvany.exe
# and pnp_wait.exe which are satisfied by the dependency on
# mingw32-srvany.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/virt-tools
pushd $RPM_BUILD_ROOT%{_datadir}/virt-tools
ln -sf ../../i686-w64-mingw32/sys-root/mingw/bin/rhsrvany.exe
ln -sf ../../i686-w64-mingw32/sys-root/mingw/bin/pnp_wait.exe
popd

%if 0%{?rhel}
# On RHEL remove virt-v2v-in-place.
rm $RPM_BUILD_ROOT%{_bindir}/virt-v2v-in-place
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-v2v-in-place.1*
%endif

# Find locale files.
%find_lang %{name}


%check
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
    if -s test-data/phony-guests/$f; then
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
%endif
%{_bindir}/virt-v2v-inspector
%{_mandir}/man1/virt-v2v.1*
%{_mandir}/man1/virt-v2v-hacking.1*
%{_mandir}/man1/virt-v2v-input-vmware.1*
%{_mandir}/man1/virt-v2v-input-xen.1*
%if !0%{?rhel}
%{_mandir}/man1/virt-v2v-in-place.1*
%endif
%{_mandir}/man1/virt-v2v-inspector.1*
%{_mandir}/man1/virt-v2v-output-local.1*
%{_mandir}/man1/virt-v2v-output-openstack.1*
%{_mandir}/man1/virt-v2v-output-rhv.1*
%{_mandir}/man1/virt-v2v-release-notes-1.42.1*
%{_mandir}/man1/virt-v2v-release-notes-2.0.1*
%{_mandir}/man1/virt-v2v-release-notes-2.2.1*
%{_mandir}/man1/virt-v2v-support.1*
%{_datadir}/virt-tools


%files bash-completion
%license COPYING
%{_datadir}/bash-completion/completions/virt-v2v


%files man-pages-ja
%license COPYING
%lang(ja) %{_mandir}/ja/man1/*.1*


%files man-pages-uk
%license COPYING
%lang(uk) %{_mandir}/uk/man1/*.1*


%changelog
* Sun Apr 09 2023 Laszlo Ersek <lersek@redhat.com> - 1:2.2.0-6
- cope with kernel-core / kernel-modules-core subpackage split in RHEL-9.2 guests
  resolves: rhbz#2184970
* Mon Feb 06 2023 Richard W.M. Jones <rjones@redhat.com> - 1:2.2.0-5
- Rebase to virt-v2v 2.2.0
  resolves: rhbz#2135762
- Copy drivers for Windows 11, Windows 2019 & Windows 2022
  resolves: rhbz#2149811
- Fix Description field for Windows >= 10 in -o rhv/vdsm modes
  resolves: rhbz#2149863
- Fix UEFI fallback boot loader if broken
  resolves: rhbz#2149629
- Document Windows system on Dynamic Disk is not supported (2140548 comment 5)
- Include the BOCHS DRM driver in the initial ram disk
  resolves: rhbz#2131123
- windows_virtio: favor "fwcfg" over "qemufwcfg"
  resolves: rhbz#2151752
- -o rhv-upload: set ovirt:id correctly
  resolves: rhbz#2152465
- Enable the %%check tests
- -o kubevirt: Fix position of cpu field
  resolves: rhbz#2162331
- -o kubevirt: Fix incorrect error message
  resolves: rhbz#2162441
- -o kubevirt: Error if invalid guest name on target
  resolves: rhbz#2162332
- -o kubevirt: Enable -oo compressed option
  resolves: rhbz#2162444
- Remove -oo qemu-boot option completely
  resolves: rhbz#2166565
- Remove warning when converting Rocky Linux
  resolves: rhbz#2166618
- Fix kernel panic after converting Rocky Linux 9
  resolves: rhbz#2166619

* Thu Aug 18 2022 Laszlo Ersek <lersek@redhat.com> - 1:2.0.7-6
- Install qemu-ga package during conversion
  resolves: rhbz#2028764

* Wed Aug 10 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.7-5
- Remove LVM2 "devices file" during conversion
  resolves: rhbz#2112801
- Add support for Zstandard compressed kernel modules
  resolves: rhbz#2116811

* Fri Jul 29 2022 Laszlo Ersek <lersek@redhat.com> - 1:2.0.7-4
- Remove legacy crypto advice and replace with targeted mechanism
  resolves: rhbz#2062360

* Mon Jul 25 2022 Laszlo Ersek <lersek@redhat.com> - 1:2.0.7-3
- relax qemu64 VCPU feature checking in the libvirt output
  resolves rhbz#2107503

* Fri Jul 15 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.7-2
- Rebase to stable branch version 2.0.7
  resolves: rhbz#2059287, rhbz#1658126, rhbz#1788823, rhbz#1854275
- Fix openssh-clients dependency
  resolves: rhbz#2064178
- Fix security issue when running virt-v2v as root
  resolves: rhbz#2066773
- Remove -o json mode
  resolves: rhbz#2074026
- Allow conversion of guests with NVMe drives from VMX files
  resolves: rhbz#2070530
- Cleanly reject guests with snapshots when using -it ssh
  resolves: rhbz#1774386
- Document that vmx+ssh "-ip" auth doesn't cover ssh / scp shell commands
  resolves: rhbz#1854275
- Fix conversion if swap partition isn't encrypted with root directory
  resolves: rhbz#1658128
- Document permissions when importing OVA using RHV UI
  resolves: rhbz#2039597
- Multiple fixes for -o qemu mode
  resolves: rhbz#2074805
- Work around blocking bug in OpenStack
  resolves: rhbz#2074801
- If multiple open-vm-tools packages are installed, remove all (2076436)
- For -o rhv-upload wait for VM creation task
  resolves: rhbz#1985830
- For -i vmx add full support for SATA hard disks
  resolves: rhbz#1883802
- Fix booting of RHEL 9.1 guests after conversion
  resolves: rhbz#2076013
- Fix -o qemu warning
  resolves: rhbz#2082603
- If listing RPM applications fails, rebuild DB and retry (2089623)
- Document -i vmx -it ssh percent encoding in ssh URIs
  resolves: rhbz#1938954
- Document extra permissions needed for VMware 7 (1817050)
- Remove osprober devices left around by grub2
  resolves: rhbz#2003503
- Add Requires python3 / platform-python
  resolves: rhbz#2094779
- Fix CVE-2022-2211 Denial of Service in --key parameter
  resolves: rhbz#2102719
- Add -oo compressed support
  resolves: rhbz#2047660
- Limit the maximum of disks per guest
  resolves: rhbz#2051564
- Add support for LUKS encrypted guests using Clevis & Tang
  resolves: rhbz#1809453
- Fix remapping of nvme devices in /boot/grub2/device.map
  resolves: rhbz#2101665
- Improve documentation of vmx+ssh and -ip option
  resolves: rhbz#1854275
- Fix race condition when unmounting in -o rhv mode (1953286#c26)

* Tue Feb 15 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.99-1
- Rebase to upstream 1.45.99.
- Add check for sufficient free space in the host
  resolves: rhbz#2051394
- Update documentation of -ip for conversions from VMware over HTTPS
  related: rhbz#1960087
- -o rhv-upload: Keep connections alive
  resolves: rhbz#2032324
- -o rhv-upload: Improve conversion performance
  resolves: rhbz#2039255
- -o rhv-upload: Replace -oo rhv-direct with -oo rhv-proxy
  resolves: rhbz#2033096
- Fix log line wrapping making log parsing difficult (1820221)

* Wed Feb 2 2022 Laszlo Ersek <lersek@redhat.com> - 1:1.45.97-4
- v2v import from vCenter fails when using interactive password because
  cookie-script tries to be interactive
  (pick commit 8abc07a8589a)
  resolves: rhbz#1960087
- model='virtio-transitional' is wrongly added when converting windows
  guest to local by rhel9 v2v
  (pick commit range commit range 8abc07a8589a..cacedec64072)
  resolves: rhbz#2043333

* Wed Jan 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.97-3
- Rebase to upstream 1.45.97.
  resolves: rhbz#2011713
- Add virtio-transitional for older guests when converting to q35
  resolves: rhbz#1942325
- Fix -o rhv mode
  resolves: rhbz#2027598
- input: xen: Fix assertion error when importing from remote block device
  resolves: rhbz#2041852
- output: -o json: Allow -oo (output options) to work
  resolves: rhbz#2041850
- Fix virt-v2v hang when given incorrect vpx:// URL
  resolves: rhbz#2041886
- Fix hang when converting with virt-p2v
  resolves: rhbz#2044911
- Send nbdinfo debugging information to stderr
  resolves: rhbz#2044922
- Explicitly require platform-python
  resolves: rhbz#2046178

* Thu Dec 23 2021 Laszlo Ersek <lersek@redhat.com> - 1:1.45.95-3
- output_rhv: restrict block status collection to the old RHV output
- Rebase from upstream commit 702a511b7f33 to direct child commit 07b12fe99fb9
  resolves: rhbz#2034240

* Sat Dec 18 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.95-2
- Rebase to upstream 1.45.95.
- Change video type to VGA (instead of QXL).
- Remove --in-place support properly.
- Remove -o glance support properly.
- Fix quoting with openssh >= 8.7 (RHEL) / 8.8
- Fix q35 error "IDE controllers are unsupported"
- Add virt-v2v and libvirt version in debug output
- Fix -o rhv output mode showing no guests listed
  resolves: rhbz#2011713, rhbz#1961107, rhbz#2027673,
  rhbz#1637857, rhbz#2032112, rhbz#2027598

* Wed Aug 18 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.3-3
- Fix conversion of Windows BitLocker guests
  resolves: rhbz#1994984

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1:1.45.3-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Aug 06 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.3-1
- New upstream development version 1.45.3.
- Rebase RHEL patches.
  resolves: rhbz#1950634

* Wed Jun 30 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.2-1
- New upstream development version 1.45.2.
- Remove --debug-overlays and --print-estimate options.
- Remove -o glance option on RHEL 9 (RHBZ#1977539).
- Remove support for RHEV-APT (RHBZ#1945549).

* Wed Jun 16 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.1-1.el9.1
- New upstream development version 1.45.1.
- Require virtio-win on RHEL (RHBZ#1972644).
- v2v-test-harness, virt-v2v-copy-to-local have been removed upstream.

* Thu Jun 10 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.44.0-2
- nbdkit-vddk-plugin dep only exists on x86-64.

* Mon May 10 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.44.0-1.el9.1
- Rebuild in RHEL 9 against libguestfs 1.45.5
  resolves: rhbz#1959042

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
