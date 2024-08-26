// flask_ml_app/static/js/main.js

$(document).ready(function() {
    $('#predictionForm').on('submit', function(event) {
            event.preventDefault();

                    $.ajax({
                                url: '/predict',
                                            type: 'POST',
                                                        data: { input_data: $('#input_data').val() },
                                                                    success: function(response) {
                                                                                    $('#result').text(response.prediction);
                                                                                                }
                                                                                                        });
                                                                                                            });
                                                                                                            });