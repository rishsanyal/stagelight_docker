import React, { useEffect } from 'react';
import { useSearchParams } from "react-router-dom";

import { getSpecificTopicsList, getUserSubmission } from '../../redux/actions/TopicsActions';

// import Accordion from '@mui/material/Accordion';
// import AccordionSummary from '@mui/material/AccordionSummary';
// import AccordionDetails from '@mui/material/AccordionDetails';
// import Typography from '@mui/material/Typography';
// import { FileDownload } from "@mui/icons-material";

import { Editor } from "react-draft-wysiwyg";
import "react-draft-wysiwyg/dist/react-draft-wysiwyg.css";
import { EditorState, ContentState } from 'draft-js';

import Cookies from 'js-cookie';

function CustomOption(props) {
    return (
        <div>
            <button onClick={props.onClick}>submit</button>
        </div>
    );
}

function TopicSubmission() {

    const [searchParams, setSearchParams] = useSearchParams();
    var topicId = searchParams.get("topicId");
    const [editorState, setEditorState] = React.useState(EditorState.createEmpty());
    const username = Cookies.get('username')
    const [userSubmitted, setUserSubmitted] = React.useState(false);

    const [topic, setTopic] = React.useState({
        title: "",
        upvotes: 0,
        downvotes: 0,
    });

    useEffect(() => {
        let mounted = true;

        getSpecificTopicsList(topicId).then(items => {
            if(mounted) {
                setTopic(items)
            }
        }).then(() => {
            console.log(topic);
        })

        getUserSubmission(username, topicId).then(items => {
            if(mounted) {
                if (items) {
                    setEditorState(EditorState.createWithContent(ContentState.createFromText(items)));
                    setUserSubmitted(true);
                }
            }
        })

        return () => mounted = false;
    }, []);

    const style={
        display: "flex",
        gap: "10px",
    }

    const onEditorStateChange = (editorState) => {
        setEditorState(editorState);
    };

    const submit = (topicID) => {
        var plainText = editorState.getCurrentContent().getPlainText();

        fetch('http://localhost:8000/topics/submission/', {
            method: 'POST',
            body: JSON.stringify({
                id: topicID,
                textEntry: plainText,
                username: username
            }),
            headers: {
              'Content-type': 'application/json; charset=UTF-8',
            },
          }).then((response) => {
            console.log(response.data);
            if (response.status === 201 || response.status === 200) {
                setUserSubmitted(true);
            }
          }).catch((error) => {
            console.log(error);
          })
    }

    return (
        <div>
            <div>
                {topic.title}
            </div>
            <div  style={style}>
                <div>
                    Upvotes: {topic.upvotes}
                </div>
                <div>
                    Downvotes: {topic.downvotes}
                </div>
            </div>
            <div>
                <Editor
                    editorStyle={{ height: '400px'}}
                    editorState={editorState}
                    wrapperClassName="demo-wrapper"
                    editorClassName="demo-editor"
                    onEditorStateChange={onEditorStateChange}
                    toolbarCustomButtons={[<CustomOption onClick={() => submit(topic.id)}/>]}
                />
            </div>

        </div>
    )
}

export default TopicSubmission