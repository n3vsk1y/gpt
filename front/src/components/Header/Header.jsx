import './Header.css'

import VersionOption from '../VersionOption'

import { versions } from '../../data/versions'
import logo from '../../assets/logo.svg'

export default function Header() {
	return (
		<header>
			<img src={logo} />
			<select>
                {versions.map((version) => (
                    <VersionOption {...version} />
                ))}
			</select>
		</header>
	)
}