Name:           antimicro
Version:        2.4
Release:        1%{?dist}
Summary:        Graphical program used to map keyboard keys and mouse controls to a gamepad

License:        GPLv3+
URL:            https://github.com/Ryochan7/antimicro
Source0:        https://github.com/Ryochan7/antimicro/archive/%{version}.tar.gz

BuildRequires:  SDL2-devel, qt-devel, libXtst-devel, libX11-devel, cmake

%description
AntiMicro is a graphical program that can be used to map keyboard
keys and mouse controls to a gamepad. This functionality is useful
for playing games with no built-in or poor gamepad support.

%prep
%setup -q


%build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX="/usr" -DUSE_SDL_2=1 ..
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd build
cmake ..
make DESTDIR=%{buildroot} install
cd ..
%find_lang antimicro --with-qt


%files -f %{name}.lang
%doc
%{_bindir}/antimicro
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.gz



%changelog
* Fri May 30 2014 Travis Nickles <nickles.travis@gmail.com> - 2.4-1
- Updated to version 2.4

* Fri May 23 2014 Travis Nickles <nickles.travis@gmail.com> - 2.3.3-1
- Updated to version 2.3.3

* Thu May 15 2014 Travis Nickles <nickles.travis@gmail.com> - 2.3.2-1
- Updated to version 2.3.2

* Tue May 13 2014 Travis Nickles <nickles.travis@gmail.com> - 2.3.1-1
- Updated to version 2.3.1

* Fri May 02 2014 Travis Nickles <nickles.travis@gmail.com> - 2.3-1
- Updated to version 2.3

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

