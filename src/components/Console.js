import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
// import Paper from "@material-ui/core/Paper";
// import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";

const styles = theme => ({
  root: {
    ...theme.mixins.gutters(),
    paddingTop: theme.spacing.unit * 2,
    paddingBottom: theme.spacing.unit * 2
  }
});

function PaperSheet(props) {
  const { classes } = props;
  console.log(
    "👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀"
  );
  console.log(classes);
  console.log(
    "👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀"
  );

  const divStyle = {
    "margin-top": "100%"
  };

  const bottomStyle = {
    position: "absolute",
    bottom: 0,
    left: 0
  };

  return (
    <div>
      <div />
      <div style={bottomStyle}>
        <TextField
          multiline={true}
          autoFocus={true}
          rows={30}
          fullWidth={true}
        />
      </div>
    </div>
  );
}

PaperSheet.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(PaperSheet);
