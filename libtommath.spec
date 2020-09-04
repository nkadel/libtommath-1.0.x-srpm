Name:           libtommath
Version:        1.0.1
#Release:        4%%{?dist}
Release:        0.1%{?dist}
Summary:        A portable number theoretic multiple-precision integer library
License:        Public Domain
URL:            http://www.libtom.net/

Source0:        https://github.com/libtom/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Requies PowerTools on Centtos 8
BuildRequires:  ghostscript
BuildRequires:  libtiff-tools
BuildRequires:  libtool
BuildRequires:  texlive-dvips-bin
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  texlive-makeindex-bin
BuildRequires:  texlive-mfware-bin
%if 0%{?rhel} == 8
BuildRequires:	texlive-metafont
%endif
BuildRequires:  tex(cmr10.tfm)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(hyphen.tex)

%description
A free open source portable number theoretic multiple-precision integer library
written entirely in C. (phew!). The library is designed to provide a simple to
work with API that provides fairly efficient routines that build out of the box
without configuration.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
Provides:       %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < 0.42-1

%description    doc
The %{name}-doc package contains PDF documentation for using %{name}.

%prep
%setup -q
# Fix permissions on installed library
sed -i -e 's/644 $(LIBNAME)/755 $(LIBNAME)/g' makefile.shared
# Fix pkgconfig path
sed -i \
    -e 's|^prefix=.*|prefix=%{_prefix}|g' \
    -e 's|^libdir=.*|libdir=%{_libdir}|g' \
    %{name}.pc.in

%build
%make_build V=1 CFLAGS="%{optflags} -I./" -f makefile.shared
%make_build V=1 -f makefile poster
%if 0%{?rhel} != 8
%make_build V=1 -f makefile manual
%endif
%make_build V=1 -f makefile docs

%install
%make_install V=1 CFLAGS="%{optflags} -I./" PREFIX=%{_prefix} LIBPATH=%{_libdir} -f makefile.shared

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

#%%ldconfig_scriptlets
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%if 0%{?rhel} != 8
%doc doc/bn.pdf
%endif
%doc doc/poster.pdf
%doc doc/tommath.pdf

%changelog
* Sat Sep 5 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 1.0.1-0.1
- Discard BuildRequires for epel-rpm-macros

* Tue May 14 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.0.1-0
- Disabling building bn.pdf on RHEL 8
- Add BuildRequires for texlive-metafont to get /usr/bin/mf

* Sun Feb 25 2018 Florian Weimer <fweimer@redhat.com> - 1.0.1-4
- Add BuildRequires: ghostscript-tools-dvipdf

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Switch to %%ldconfig_scriptlets

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 1.0.1-1
- Update to 1.0.1.
- Trim changelog.
- Clean up SPEC file.
- Remove RHEL 6 support.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Simone Caronni <negativo17@gmail.com> - 1.0-7
- Update URL (#1463608, #1463547).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Simone Caronni <negativo17@gmail.com> - 1.0-4
- Fix installs with non-standard buildroots (#1299860).

* Tue Feb 23 2016 Simone Caronni <negativo17@gmail.com> - 1.0-3
- Remove useless latex build requirements.

* Tue Feb 23 2016 Simone Caronni <negativo17@gmail.com> - 1.0-2
- Use proper source URL.
- Cleanup SPEC file.

* Tue Feb 23 2016 Simone Caronni <negativo17@gmail.com> - 1.0-1
- Fix FTBFS (#1307741).
- Update to 1.0.
- Update URL.
- Use license macro.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
