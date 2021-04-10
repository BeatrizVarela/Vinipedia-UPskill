const initialState = {
    wines: []
}

export default function loadReducer (state=initialState, action) {
    switch (action.type) {
        case 'DATA' :
            return {
                ...state,
                wines: [...state.wines, ...action.payload]
            }
        default:
            return {...state};
    }
}