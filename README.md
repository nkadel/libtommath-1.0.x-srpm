libtommath-1.0.x-srpm
=====================

SRPM building tools for libtommath for Samba 4 on RHEL 8.

This tool taken from the EPEL 7 release. It had to be modified to
exclude building certain documents due to tetex failurs on RHEL 8.

The "make" command will do these steps.

	make build	# Build the package on the local OS
	make all	# Use "mock" to build the packages with the local
			# samba4repo configuration, which needs.
	make install	# Actually install the RPM's in the designated
			# location for samba4repo


		Nico Kadel-Garcia <nkadel@gmail.com>
