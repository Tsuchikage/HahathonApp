import { AppShell, Button, TextInput, TextInputProps } from '@mantine/core'
import classes from './MobileNavbar.module.css'
import Logo from '../common/Logo'
import { Link, Outlet, useLocation } from 'react-router-dom'
import { IconSearch } from '@tabler/icons-react'

const SearchInput = (props: TextInputProps) => {
	const icon = <IconSearch style={{ width: 16, height: 16 }} />

	return (
		<TextInput
			variant="filled"
			placeholder="Искать людей"
			leftSection={icon}
			style={{ marginInline: 'auto' }}
			{...props}
		/>
	)
}

const LoginButton = () => {
	return (
		<Link to="auth">
			<Button w={80}>Войти</Button>
		</Link>
	)
}

const MobileNavbar = () => {
	const location = useLocation()

	const isAuth = location.pathname === '/auth'

	return (
		<AppShell header={{ height: 60 }} padding="md">
			<AppShell.Header className={classes.header}>
				<div
					className={classes.inner}
					style={{ paddingRight: isAuth ? 80 : 0 }}
				>
					<Logo size={28} />
					<SearchInput />
					{!isAuth && <LoginButton />}
				</div>
			</AppShell.Header>
			<AppShell.Main>
				<Outlet />
			</AppShell.Main>
		</AppShell>
	)
}

export default MobileNavbar
