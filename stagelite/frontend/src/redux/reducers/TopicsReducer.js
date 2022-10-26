import { FETCH_TOPICS } from "../ActionTypes";
// import asyncComponent from "../AsyncComponent";

const initialState = {
    topics: [],
    loading: false,
}

function TopicsReducer(state = initialState, action) {
    switch (action.type) {
        case FETCH_TOPICS:
            const userAction = async () => {
                // const response = await fetch('http://0.0.0.0:8000/topics/topics_list', {method:'GET',
                // headers: {'Authorization': 'Basic ' + btoa('froot:password')}});
                let response = await fetch('http://0.0.0.0:8000/topics/topics_list', {method:'GET',
                    headers: {'Authorization': 'Basic ' + btoa('froot:password')}});
                let data = await response.json();
                state.topics = data;
              }
            userAction();
            console.log(state.topics);
            return {
                ...state,
                loading: true
            }
        default:
            return state;
    }
}

export default TopicsReducer;