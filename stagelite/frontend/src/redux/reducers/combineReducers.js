import { combineReducers, createStore } from 'redux';
import TopicsReducer from './TopicsReducer';

export const rootReducer = combineReducers({
    topics: TopicsReducer,
});

export const store = createStore(
    rootReducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

// export const store = configureStore({
//     reducer: {
//         topics: TopicsReducer,
//     },
// });
