import React, { useEffect } from 'react'

import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import { FileDownload } from "@mui/icons-material";
import Button from '@mui/material/Button';

import {voteTopic} from '../../redux/actions/TopicsActions';


//create your forceUpdate hook
function useForceUpdate(id, voteType){
  voteTopic(id, voteType)
  const [value, setValue] = React.useState(0); // integer state
  return () => setValue(value => value + 1); // update state to force render
  // An function that increment 👆🏻 the previous state like here
  // is better than directly setting `value + 1`
}

export function TopicDisplay({title, upvotes, downvotes, id, userentry, update, setUpdate}) {

  var style = {};
  const [upvote, setUpvote] = React.useState(upvotes);
  const [downvote, setDownvote] = React.useState(downvotes);

  if (userentry) {
    style = {
      backgroundColor: "#ffc6c4"
    }
  } else {
    style = {
      backgroundColor: "lightgreen"
    }
  }

  const updateVote = (id, voteType) => {
    if (voteType === "upvote") {
      setUpvote(upvote + 1)
    } else {
      setDownvote(downvote + 1)
    }
    voteTopic(id, voteType);
    setUpdate(!update);
  }

  return (
    <div style={{display: "flex"}}>
        <Accordion style={style}>
        <AccordionSummary
          expandIcon={<FileDownload />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography>Topic #{id}</Typography>
        </AccordionSummary>
        <AccordionDetails>
          {userentry === false ?
          <a href={`/topicSubmission?topicId=${id}`}>
          <Typography>
            {title}
          </Typography>
          </a> :
          <Typography>
            {title}
          </Typography>
      }

        </AccordionDetails>
        </Accordion>
        {/* {title}

        <div>
            {upvotes}
            {downvotes}
        </div> */}


        <Button onClick={() => updateVote(id, "upvote")}>↑ {upvotes}</Button>
        <Button onClick={() => updateVote(id, "downvote")}>↓ {downvotes}</Button>
    </div>
  )
}

export default TopicDisplay