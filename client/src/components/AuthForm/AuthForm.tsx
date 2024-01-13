import { useToggle } from '@mantine/hooks'
import { useForm } from '@mantine/form'
import {
	TextInput,
	PasswordInput,
	Text,
	Paper,
	PaperProps,
	Button,
	Anchor,
	Stack
} from '@mantine/core'

import classes from './AuthForm.module.css'
import classNames from 'classnames'
import { useNavigate } from 'react-router-dom'
import { createEffect } from '../../lib/state-engine'
import { post } from '../../lib/api'

const login = createEffect(async (body: AuthPayload) => {
	const data = await post('/api/auth/token', body)
	return data
})

const AuthForm = ({ className, ...props }: PaperProps) => {
	const navigate = useNavigate()

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

	const handleOnSubmit = (e: AuthPayload) => {
		console.log(e)

		login(e)
	}

	return (
		<Paper
			display="flex"
			p="lg"
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
						value={form.values.username}
						onChange={event =>
							form.setFieldValue('username', event.currentTarget.value)
						}
						error={
							form.errors.username &&
							'Имя пользователя должно содержать не менее 6 символов'
						}
						radius="lg"
					/>
					<PasswordInput
						required
						placeholder="Пароль"
						value={form.values.password}
						onChange={event =>
							form.setFieldValue('password', event.currentTarget.value)
						}
						error={
							form.errors.password &&
							'Пароль должен содержать не менее 6 символов'
						}
						radius="lg"
					/>
				</Stack>

				<Stack mt="xl" align="start">
					<Button color="dark" radius="lg" type="submit" w="100%">
						{type === 'register' ? 'Создать аккаунт' : 'Войти'}
					</Button>
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
				</Stack>
			</form>
		</Paper>
	)
}

export default AuthForm

type AuthPayload = {
	username: string
	password: string
}
