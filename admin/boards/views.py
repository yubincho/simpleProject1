from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Board
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.


def board_detail(request, board_id):
    try:
        board_detail = Board.objects.get(pk=board_id)

    except Board.DoesNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")
    # print(course_id)

    return render(request, "board_detail.html", {"board": board_detail})


def board_list(request):
    all_boards = Board.objects.all().order_by("-id")

    page = int(request.GET.get("p", 1))
    paginator = Paginator(all_boards, 5)

    boards = paginator.get_page(page)

    def get_object(self):
        object = super(board_list, self).get_object()
        object.hit += 1
        object.save()
        return object

    return render(request, "board_list.html", {"boards": boards})


def search_result(request):

    boards = Board.objects.all().order_by("-id")
    # qs = Board.objects.all()
    search = request.GET.get("search")

    if not search == "" and search is not None:
        boards = boards.filter(title__icontains=search)

    return render(request, "search_result.html", {"boards": boards})


"""
    search = request.GET.get("search", "")
    render_args = {
        "search": search,
    }

    if not search == "":
        searches = Board.objects.order_by("created_date").reverse()

        search_result = searches.filter(
            Q(title__contains=search) | Q(content__contains=search)
        )
        render_args["search_result"] = search_result

    return render(request, "result.html", render_args)
"""
