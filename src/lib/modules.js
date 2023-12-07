const modules = {
    try_json_parse: function(json_str)
    {
        try
        {
            JSON.parse(json_str);

            return true;
        }
        catch (err)
        {
            return false;
        }
    }
};




export default modules;