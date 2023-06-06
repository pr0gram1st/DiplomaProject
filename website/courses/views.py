from django.shortcuts import render

def course(request, course_id):
    course_title = 'Programming'
    video_url = 'https://www.youtube.com/embed/HHx3tTQWUx0'
    text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. "
    links = {'https://docs.djangoproject.com/en/4.2/intro/tutorial01/':'Django First Lesson', 'https://docs.djangoproject.com/en/4.2/intro/tutorial02/':'Django Second Lesson', 'https://docs.djangoproject.com/en/4.2/intro/tutorial03/': 'Django Third Lesson'}
    return render(request, 'base.html', {
        "course_title" : course_title,
        "video_url" : video_url,
        "text" : text,
        "links" : links,
        "course_id" : course_id
    })