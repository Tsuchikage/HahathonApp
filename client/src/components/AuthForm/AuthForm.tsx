<<<<<<< HEAD
import { useToggle } from '@mantine/hooks'
=======
import { useToggle, upperFirst } from '@mantine/hooks'
>>>>>>> c9c4eb3 (add: vite.js)
import { useForm } from '@mantine/form'
import {
	TextInput,
	PasswordInput,
	Text,
	Paper,
<<<<<<< HEAD
=======
	Group,
>>>>>>> c9c4eb3 (add: vite.js)
	PaperProps,
	Button,
	Anchor,
	Stack
} from '@mantine/core'

import classes from './AuthForm.module.css'
import classNames from 'classnames'
<<<<<<< HEAD
import { useNavigate } from 'react-router-dom'
import { createEffect } from '../../lib/state-engine'
import { post } from '../../lib/api'

const login = createEffect(async (body: AuthPayload) => {
	const data = await post('/api/auth/token', body)
	return data
})

const AuthForm = ({ className, ...props }: PaperProps) => {
	const navigate = useNavigate()

=======

const AuthForm = ({ className, ...props }: PaperProps) => {
>>>>>>> c9c4eb3 (add: vite.js)
	const [type, toggle] = useToggle(['login', 'register'])
	const form = useForm({
		initialValues: {
			username: '',
			password: ''
		},

		validate: {
			username: val =>
				val.length <= 6
					? 'Имя пользователя должно содержать не менее 6 символов'
					: null,
			password: val =>
				val.length <= 6 ? 'Пароль должен содержать не менее 6 символов' : null
		}
	})

<<<<<<< HEAD
	const handleOnSubmit = (e: AuthPayload) => {
		console.log(e)

		login(e)
	}

=======
>>>>>>> c9c4eb3 (add: vite.js)
	return (
		<Paper
			display="flex"
			p="lg"
<<<<<<< HEAD
			className={classNames(classes.auth, className)}
			{...props}
		>
			<Text size="lg" fw={500} tt="uppercase" ta="center">
				Добро пожаловать
			</Text>

			<form onSubmit={form.onSubmit(handleOnSubmit)}>
				<Stack>
					<TextInput
						required
						placeholder="Имя пользователя"
=======
			withBorder
			className={classNames(classes.auth, className)}
			{...props}
		>
			<Text size="lg" fw={500}>
				Добро пожаловать
			</Text>

			<form onSubmit={form.onSubmit(() => {})}>
				<Stack>
					<TextInput
						label="Имя пользователя"
						placeholder="johndoe"
>>>>>>> c9c4eb3 (add: vite.js)
						value={form.values.username}
						onChange={event =>
							form.setFieldValue('username', event.currentTarget.value)
						}
<<<<<<< HEAD
						error={
							form.errors.username &&
							'Имя пользователя должно содержать не менее 6 символов'
						}
						radius="lg"
					/>
					<PasswordInput
						required
						placeholder="Пароль"
=======
					/>
					<PasswordInput
						required
						label="Пароль"
						placeholder="Ваш пароль"
>>>>>>> c9c4eb3 (add: vite.js)
						value={form.values.password}
						onChange={event =>
							form.setFieldValue('password', event.currentTarget.value)
						}
						error={
							form.errors.password &&
							'Пароль должен содержать не менее 6 символов'
						}
<<<<<<< HEAD
						radius="lg"
					/>
				</Stack>

				<Stack mt="xl" align="start">
					<Button color="dark" radius="lg" type="submit" w="100%">
						{type === 'register' ? 'Создать аккаунт' : 'Войти'}
					</Button>
=======
					/>
				</Stack>

				<Group justify="space-between" mt="xl">
>>>>>>> c9c4eb3 (add: vite.js)
					<Anchor
						component="button"
						type="button"
						c="dimmed"
						onClick={() => toggle()}
						size="xs"
					>
						{type === 'register'
							? 'Есть аккаунт? Войти'
							: 'Нет аккаунта? Регистрация'}
					</Anchor>
<<<<<<< HEAD
				</Stack>
=======
					<Button type="submit">
						{upperFirst(type === 'register' ? 'Создать аккаунт' : 'Войти')}
					</Button>
				</Group>
>>>>>>> c9c4eb3 (add: vite.js)
			</form>
		</Paper>
	)
}

export default AuthForm
<<<<<<< HEAD

type AuthPayload = {
	username: string
	password: string
}
=======
>>>>>>> c9c4eb3 (add: vite.js)
