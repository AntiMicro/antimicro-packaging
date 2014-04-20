Name:           antimicro
Version:        2.2
Release:        1%{?dist}
Summary:        Graphical program used to map keyboard keys and mouse controls to a gamepad

License:        GPLv3+
URL:            https://github.com/Ryochan7/antimicro
Source0:        https://github.com/Ryochan7/antimicro/archive/2.2.tar.gz

BuildRequires:  SDL2-devel, qt-devel, libXtst-devel, libX11-devel

%description
AntiMicro is a graphical program that can be used to map keyboard
keys and mouse controls to a gamepad. This functionality is useful
for playing games with no built-in or poor gamepad support.

%prep
%setup -q


%build
cd src
qmake-qt4 INSTALL_PREFIX="/usr" USE_SDL_2=1 antimicro.pro
make %{?_smp_mflags}


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
* Sat Apr 19 2014 Travis Nickles <nickles.travis@gmail.com> - 2.2-1
- Updated to version 2.2

* Fri Feb 28 2014 Travis Nickles <nickles.travis@gmail.com> - 2.1-1
- Updated to version 2.1

* Sat Jan 04 2014 Travis Nickles <nickles.travis@gmail.com> - 2.0-1
- Updated to version 2.0

* Fri Dec 13 2013 Travis Nickles <nickles.travis@gmail.com> - 1.2-1
- Updated to version 1.2

* Fri Oct 04 2013 Travis Nickles <nickles.travis@gmail.com> - 1.1-1
- Initial version of the package

