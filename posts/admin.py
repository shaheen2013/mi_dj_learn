from django.contrib import admin
from posts.models import Post, Category, PostSeo
from django.template.defaultfilters import truncatewords_html, striptags
from django.utils.html import format_html, mark_safe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ['title', 'slug']
    save_as = False
    save_as_continue = False


class PostSeoInline(admin.StackedInline):
    model = PostSeo
    min_num = 1
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'view_content', 'image_tag', 'show_seo_contents', 'action_column']

    list_display_links = None

    change_form_template = 'change_form.html'

    ordering = ['id']

    inlines = [
        PostSeoInline,
    ]

    # Customize Default Fields
    @admin.display(empty_value='---')
    def view_content(self, obj):
        return format_html(truncatewords_html(striptags(obj.content), 10))

    view_content.short_description = 'Content'

    # Show image on admin table
    def image_tag(self, obj):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (obj.image))

    image_tag.short_description = 'Image'

    # Show action column
    def action_column(self, obj):
        return mark_safe(
            '<a href="/admin/posts/post/%s/change">Edit</a> '
            '<a href="/admin/posts/post/%s/delete/" style="color:red; margin-left: 5px;">Delete</a>'
            % (obj.id, obj.id)
        )

    action_column.short_description = 'Action'

    # Show Seo contents
    def show_seo_contents(self, obj):
        html = ''
        for seo in obj.postseo_set.all():
            html += mark_safe(
                '<li>'
                '<p><strong>Title:</strong> %s</p>'
                '<p><strong>Description:</strong> %s</p>'
                '</li>'
                % (seo.title, seo.description))

        return mark_safe('<ul>%s</ul>' % (html))

    show_seo_contents.short_description = 'Seo Contents'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
