import React from 'react'

import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import { FileDownload } from "@mui/icons-material";

export function TopicDisplay({title, upvotes, downvotes, id}) {
  return (
    <div>
        <Accordion>
        <AccordionSummary
          expandIcon={<FileDownload />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography>Topic #{id}</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <a href={`/topicSubmission?topicId=${id}`}>
          <Typography>
            {title}
          </Typography>
          </a>
        </AccordionDetails>
        </Accordion>
        {/* {title}

        <div>
            {upvotes}
            {downvotes}
        </div> */}
    </div>
  )
}

export default TopicDisplay