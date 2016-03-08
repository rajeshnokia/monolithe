{{ header }}

@import <Foundation/Foundation.j>
@import <AppKit/CPArrayController.j>
@import <Bambou/NURESTObject.j>

{% for api in specification.child_apis -%}
{% set child_spec = specification_set[api.rest_name] -%}
@import "Fetchers/{{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher.j"
{% endfor -%}
{% if constants|length %}
{% for name, constant_value in constants.iteritems()|sort -%}
{{ name }} = @"{{ constant_value }}";
{% endfor -%}
{% endif %}

/*!
    {{ specification.description }}
*/
@implementation {{ class_prefix }}{{ specification.entity_name }} : NURESTObject
{
    {% for attribute in specification.attributes -%}
    /*!
        {{ attribute.description }}
    */
    {{ attribute.local_type }} _{{attribute.local_name }} @accessors(property={{attribute.local_name }});

    {% endfor %}
    {% for api in specification.child_apis -%}
    {% set child_spec = specification_set[api.rest_name] -%}
    {{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher _children{{ child_spec.entity_name_plural }} @accessors(property=children{{ child_spec.entity_name_plural }});
    {% endfor%}
}


#pragma mark -
#pragma mark Class Method

+ (CPString)RESTName
{
    return @"{{ specification.rest_name }}";
}


#pragma mark -
#pragma mark Initialization

- (id)init
{
    if (self = [super init])
    {
        {% for attribute in specification.attributes -%}
        [self exposeLocalKeyPathToREST:@"{{ attribute.local_name }}"];
        {% endfor %}
        {% for api in specification.child_apis -%}
        {% set child_spec = specification_set[api.rest_name] -%}
        _children{{ child_spec.entity_name_plural }} = [{{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher fetcherWithParentObject:self];
        {% endfor %}
    }

    return self;
}

@end
