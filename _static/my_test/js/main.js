const instruction = {
  type: "instructions",
  pages: [
    "Welcome to the experiment. Click next to begin.",
    "This is the second page of instructions.",
    "This is the final page."
  ],
  show_clickable_nav: true
};

timeline_variables = [
  {question: "100 + 200", answer: 300},
  {question: "東京スカイツリーの高さ（m）", answer: 634},
  {question: "富士山の高さ（m）", answer: 3776}
]

const response = {
  type: 'survey-text',
  questions: [{prompt: jsPsych.timelineVariable("question")}],
  on_finish: function(data) {
    document.getElementById("choice").value = data.response;
  }
};

const fixation = {
  type: 'html-keyboard-response',
  stimulus: '<div style="font-size:60px;">+</div>',
  choices: jsPsych.NO_KEYS,
  trial_duration: 1000,
}

const trial = {
  timeline: [fixation, response],
  timeline_variables: timeline_variables
}

jsPsych.init({
  timeline: [instruction, trial],
  display_element: "jspsych-target",
  // on_finish: function() {
  //   document.querySelector(".otree-btn-next").style.display = 'block';
  // }
});
