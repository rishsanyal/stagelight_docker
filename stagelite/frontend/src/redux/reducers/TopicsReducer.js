import { FETCH_TOPICS } from "../ActionTypes";
// import asyncComponent from "../AsyncComponent";

const initialState = {
    topics_input: [],
    loading: "false",
}

function TopicsReducer(state = initialState, action) {
    switch (action.type) {
        case FETCH_TOPICS:
            console.log(action.payload);
            return {
                ...state,
                topics_input: action.payload,
                loading: "here"
            }
        default:
            return state;
    }
}

export default TopicsReducer;