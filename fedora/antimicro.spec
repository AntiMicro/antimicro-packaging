Name:           antimicro
Version:        1.1
Release:        1%{?dist}
Summary:        Graphical program used to map keyboard and mouse buttons to gamepad buttons

License:        GPLv3+
URL:            https://github.com/Ryochan7/antimicro
Source0:        https://github.com/Ryochan7/antimicro/archive/1.1.tar.gz

BuildRequires:  SDL-devel, qt-devel, libXtst-devel, libX11-devel

%description
AntiMicro is a graphical program that can be used to map keyboard
and mouse buttons to gamepad button presses. This functionality is
useful for games with no gamepad support.

%prep
%setup -q


%build
cd src
qmake-qt4 INSTALL_PREFIX="/usr" antimicro.pro
make %{?_smp_mflags}
lrelease-qt4 %{name}.pro


%install
rm -rf %{buildroot}
cd src
make INSTALL_ROOT=%{buildroot} install
cd ..
%find_lang antimicro --with-qt


%files -f %{name}.lang
%doc
%{_bindir}/antimicro
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png



%changelog
* Fri Oct 04 2013 Travis Nickles <nickles.travis@gmail.com> - 1.1-1
- Initial version of the package

