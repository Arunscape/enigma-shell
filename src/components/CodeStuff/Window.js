import React from "react";
import { unstable_Box as Box } from "@material-ui/core/Box";
import Button from "@material-ui/core/Button";

function FlexDirection() {
  return (
    <div style={{ width: "100%" }}>
      <Box
        display="flex"
        flexDirection="row"
        p={1}
        m={1}
        bgcolor="background.paper"
      >
        <Box p={1} bgcolor="grey.300">
          Item 1
        </Box>
        <Box p={1} bgcolor="grey.300">
          Item 1
        </Box>
        <Box p={1} bgcolor="grey.300">
          Item 1
        </Box>
      </Box>
      <Box
        display="flex"
        flexDirection="row-reverse"
        p={1}
        m={1}
        bgcolor="background.paper"
      >
        <Box p={1} bgcolor="grey.300">
          Item 1
        </Box>
        <Box p={1} bgcolor="grey.300">
          Item 1
        </Box>
        <Box p={1} bgcolor="grey.300">
          Item 1
        </Box>
      </Box>
      <Button />
    </div>
  );
}

export default FlexDirection;
