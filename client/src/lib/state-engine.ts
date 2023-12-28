import * as effector from 'effector'
// import { attachLogger } from 'effector-logger/attach';

export * from 'effector'
export * from 'effector-react'
export const app = effector.createDomain('@mc-tlk-app')
// export const { createDomain, createStore, createEffect, createEvent } = app;
//
// if (process.env.NODE_ENV !== 'production') {
//   attachLogger(app, { inspector: 'disabled', reduxDevtools: 'disabled' });
// }
