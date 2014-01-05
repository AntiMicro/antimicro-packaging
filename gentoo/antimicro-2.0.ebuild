# Copyright 1999-2013 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=5
inherit qt4-r2

DESCRIPTION="Graphical program used to map keyboard keys and mouse controls to a gamepad"
HOMEPAGE="https://github.com/Ryochan7/antimicro"
SRC_URI="https://github.com/Ryochan7/antimicro/archive/${PV}.tar.gz -> ${P}.tar.gz"

LICENSE="GPL-3"
SLOT="0"
KEYWORDS="~amd64 ~x86"
IUSE="sdl2"

DEPEND="x11-libs/libX11
		x11-libs/libXtst
		>=dev-qt/qtcore-4.8:4
		>=dev-qt/qtgui-4.8:4
		sdl2? ( media-libs/libsdl2[joystick] )
		!sdl2? ( =media-libs/libsdl-1.2*[joystick] )"
RDEPEND="${DEPEND}"

S=${WORKDIR}/${P}/src

src_configure() {
	if use sdl2 ; then
		eqmake4 INSTALL_PREFIX=/usr USE_SDL_2=1 antimicro.pro
	else
		eqmake4 INSTALL_PREFIX=/usr antimicro.pro
	fi
}

src_compile() {
	emake 
}
