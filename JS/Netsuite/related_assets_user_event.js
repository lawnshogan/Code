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

        if (Array.isArray(relatedAssets)) {
            var formattedRelatedAssets = relatedAssets.map(function(asset) {
                return asset.text.replace(/ FAM/g, '\nFAM');
            });

            rec.setValue('custrecord_hein_inspection_related_asset', formattedRelatedAssets.join('\n'));
        }
    }

    return {
        beforeLoad: beforeLoad
    };
});
