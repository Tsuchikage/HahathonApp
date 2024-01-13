import { AppShell, Burger, Button, Group, Stack } from '@mantine/core'
import { useDisclosure } from '@mantine/hooks'
import classes from './MobileNavbar.module.css'
import Logo from '../common/Logo'
import { Outlet } from 'react-router-dom'

const links = [
	{ link: '/about', label: 'Features' },
	{ link: '/pricing', label: 'Pricing' },
	{ link: '/learn', label: 'Learn' },
	{ link: '/community', label: 'Community' }
]

const MobileNavbar = () => {
	const [opened, { toggle }] = useDisclosure()

	const items = links.map(link => (
		<a
			key={link.label}
			href={link.link}
			className={classes.link}
			onClick={event => event.preventDefault()}
		>
			{link.label}
		</a>
	))

	return (
		<AppShell
			header={{ height: 60 }}
			navbar={{
				width: 300,
				breakpoint: 'sm',
				collapsed: { desktop: true, mobile: !opened }
			}}
			padding="md"
		>
			<AppShell.Header className={classes.header}>
				<div className={classes.inner}>
					<Group>
						<Burger
							opened={opened}
							onClick={toggle}
							size="sm"
							hiddenFrom="sm"
						/>
						<Logo size={28} />
					</Group>

					<Group ml={50} gap={5} visibleFrom="sm">
						{items}
					</Group>
					<Group visibleFrom="sm">
						<Button variant="default">Log in</Button>
						<Button>Sign up</Button>
					</Group>
				</div>
			</AppShell.Header>

			<AppShell.Navbar py="md" px={4}>
				<Stack>
					<Stack gap={5}>{items}</Stack>
					<Group wrap="nowrap" px="xs">
						<Button variant="default" w="100%">
							Log in
						</Button>
						<Button w="100%">Sign up</Button>
					</Group>
				</Stack>
			</AppShell.Navbar>

			<AppShell.Main>
				<Outlet />
			</AppShell.Main>
		</AppShell>
	)
}

export default MobileNavbar
