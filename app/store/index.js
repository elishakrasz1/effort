import { createStore, combineReducers } from 'redux';
import { reducer as formReducer } from 'redux-form';

import { updateProfile, updateAction } from './actions';
import UserProfile from './reducers';

// const store = createStore(UserProfile);

const rootReducer = combineReducers({
    form: formReducer,
    userProfile: UserProfile,
    updateAction: updateAction
  });

const store = createStore(rootReducer, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__());

export default store;
export {
  updateProfile,
  updateAction
}
export { default as AmplifyBridge } from './AmplifyBridge';
