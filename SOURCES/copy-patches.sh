#!/bin/bash -

set -e

# Maintainer script to copy patches from the git repo to the current
# directory.  Use it like this:
#   ./copy-patches.sh

rhel_version=8.8.0

# Check we're in the right directory.
if [ ! -f virt-v2v.spec ]; then
    echo "$0: run this from the directory containing 'virt-v2v.spec'"
    exit 1
fi

git_checkout=$HOME/d/virt-v2v-rhel-$rhel_version
if [ ! -d $git_checkout ]; then
    echo "$0: $git_checkout does not exist"
    echo "This script is only for use by the maintainer when preparing a"
    echo "virt-v2v release on RHEL."
    exit 1
fi

# Get the base version of virt-v2v.
version=`grep '^Version:' virt-v2v.spec | awk '{print $2}'`
tag="v$version"

# Remove any existing patches.
git rm -f [0-9]*.patch ||:
rm -f [0-9]*.patch

# Get the patches.
(
  cd $git_checkout
  rm -f [0-9]*.patch

  # Ignore some directories in common/ which are not in the virt-v2v tarball.
  ignoredirs="edit mlvisit parallel progress structs visit windows"
  rm -f common/.gitattributes
  for i in $ignoredirs; do
      echo "$i/* -diff" >> common/.gitattributes
  done

  git -c core.abbrev=8 format-patch -O/dev/null --subject-prefix=PATCH -N \
      --submodule=diff --no-signature --patience $tag

  # However the .gitattributes doesn't completely ignore them but produces
  # Binary files a/... and b/... differ
  # which prevents the patches from being applied so we must remove that too.
  for i in $ignoredirs; do
      sed -i "/^diff --git a\/common\/$i/,/^Binary files a\/common\/$i/{d;}" [0-9]*.patch
  done
  rm common/.gitattributes
)
mv $git_checkout/[0-9]*.patch .

# Remove any not to be applied.
rm -f *NOT-FOR-RPM*.patch

# Add the patches.
git add [0-9]*.patch

# Print out the patch lines.
echo
echo "--- Copy the following text into virt-v2v.spec file"
echo

echo "# Patches."
for f in [0-9]*.patch; do
    n=`echo $f | awk -F- '{print $1}'`
    echo "Patch$n:     $f"
done

echo
echo "--- End of text"
