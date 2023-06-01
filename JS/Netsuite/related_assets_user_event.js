/**
 * @NApiVersion 2.x
 * @NScriptType UserEventScript
 * @NModuleScope SameAccount
 */
define([], function() {
    function beforeLoad(context) {
        if (context.type !== context.UserEventType.VIEW)
            return;

        var rec = context.newRecord;
        var relatedAssets = rec.getValue('custrecord_hein_inspection_related_asset');

        // Check if relatedAssets is a string before trying to use replace
        if (typeof relatedAssets === 'string' || relatedAssets instanceof String) {
            var formattedRelatedAssets = relatedAssets.replace(/ FAM/g, '\nFAM');
            rec.setValue('custrecord_hein_inspection_related_asset', formattedRelatedAssets);
        }
    }

    return {
        beforeLoad: beforeLoad
    };
});
