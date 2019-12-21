$(function () {
    /**
     * Set all gijgo bootstrap 4 MD datepickers
     */
    $('.gijgo-datepicker').each(function () {
        var datepickerConfig = {
            showOtherMonths: true,
            format: 'dd-mm-yyyy',  // In python we use '%d-%m-%Y'
            header: false
        };

        // if a data-min-date attribute has been set (format yyyy-mm-dd), add it to the config
        var minDate = $(this).data("min-date");
        if (minDate) {
            var md = new Date(minDate);
            datepickerConfig.minDate = new Date(
                md.getFullYear(),
                md.getMonth(),
                md.getDate()
            ); // need to construct a new date so it doesn't set the time at 13:00
        }

        $(this).datepicker(datepickerConfig);
    });

    // Initialise bsCustomFileInput to fix any Bootstrap file inputs
    bsCustomFileInput.init();
});