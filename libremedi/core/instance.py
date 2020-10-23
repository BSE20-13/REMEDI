import uuid


class ReferringObjectHelper:
    def __init__(self):
        self.list = None
        self.inst = None


class Instance:
    guid = None
    __log_format__ = None
    last_update = None
    edit_level = 0
    do_free = False
    dirty = False
    infant = True
    book = None
    # collection = None
    free_cb = None
    done_cb = None
    e_type = None

    def __init__(self, _type, book):
        assert book is not None
        assert _type is not None
        self.book = book
        col = book.get_collection(_type)
        assert col is not None
        self.e_type = _type
        if self.guid is None:
            self.guid = uuid.uuid4().hex
        while 1:
            if col.lookup_entity(self.guid) is None:
                break
            return
        self.collection = col
        col.insert_entity(self)

    def get_resident(self):
        return False

    def get_collection(self):
        return self.collection

    def set_collection(self, coll):
        self.collection = coll

    def dispose(self):
        self.e_type = None
        self.guid = None
        del self

    def guid_compare(self, other):
        if self.guid < other.guid:
            return -1
        if self.guid == other.guid: return 0
        return 1

    @classmethod
    def book_begin(cls, book):
        pass

    @classmethod
    def book_end(cls, book):
        coll = book.get_collection(cls.e_type)
        coll.destroy()

    def books_equal(self, other):
        if other is None:
            return False
        return self.book == other.book

    def set_book(self, book):
        self.book = book

    def get_book(self):
        return self.book

    def set_last_update(self, t):
        self.last_update = t

    def get_edit_level(self):
        return self.edit_level

    def increase_edit_level(self):
        self.edit_level += 1

    def decrease_edit_level(self):
        self.edit_level -= 1

    def reset_edit_level(self):
        self.edit_level = 0

    def set_destroying(self, d):
        self.do_free = d

    def get_destroying(self):
        return self.do_free

    def set_dirty_flag(self, f):
        self.dirty = f

    def get_dirty_flag(self):
        return self.dirty

    def mark_clean(self):
        self.dirty = False

    def get_dirty(self):
        return self.dirty

    def set_dirty(self):
        self.dirty = True

    def get_infant(self):
        return self.infant

    def __log__(self, flag):
        raise NotImplementedError

    @classmethod
    def __recover__(cls, data):
        raise NotImplementedError

    def begin_edit(self):
        self.edit_level += 1
        if self.edit_level > 1:
            return False
        if self.edit_level <= 0:
            self.edit_level = 1
        if self.book is None:
            return True
        be = self.book.get_backend()
        loading = False
        if be is not None:
            be.begin(self)
            loading = be.m_loading
        else:
            self.dirty = True
        return True

    def commit_edit(self):
        self.edit_level -= 1
        if self.edit_level > 0: return False
        if self.edit_level < 0:
            self.edit_level = 0
        return True

    def commit_edit_part2(self, on_error, on_done, on_free):
        from .backend import GsBackEndError
        if self.dirty and not (self.infant and self.do_free):
            self.book.mark_session_dirty()
        be = self.book.get_backend()
        if be is not None:
            errcode = be.get_error()
            while errcode != GsBackEndError.NO_ERR:
                errcode = be.get_error()
            be.commit(self)
            errcode = be.get_error()
            if errcode != GsBackEndError.NO_ERR:
                self.do_free = False
                be.set_error(errcode)
                if on_error is not None:
                    on_error(errcode)
                return False
            self.dirty = False
            if be.m_loading:
                self.do_free = False
        self.infant = False
        if be is not None:
            if self.do_free:
                if on_free is not None:
                    on_free()
                return True
            if on_done:
                on_done()
        return True

    @classmethod
    def foreach(cls, col, cb, *args):
        return col.foreach(cb, *args)

    def refers_to(self, other):
        raise NotImplementedError

    def referred(self, other):
        if self is None or other is None:
            return []
        coll = self.collection
        return self.get_referrers_from_collection(coll, other)

    @staticmethod
    def get_referring_object_instance_helper(inst, l):
        if len(l) == 0:
            l.append(inst)

    @classmethod
    def get_referring_objects_helper(cls, col, data):
        first_instance = []
        col.foreach(cls.get_referring_object_instance_helper, first_instance)
        if len(first_instance):
            new_list = first_instance[0].referred(data.inst)
            if not isinstance(new_list, list):
                raise TypeError("Function refererd has to return a list from class %s" % first_instance[0].__class__)
            data.list.extend(new_list)

    @classmethod
    def get_typed_referring_object_instance_helper(cls, inst, data):
        try:
            if cls.refers_to(inst, data.inst):
                data.list.insert(0, inst)
        except NotImplementedError:
            pass

    @classmethod
    def get_referrers_from_collection(cls, coll, ref):
        d = ReferringObjectHelper()
        d.list = []
        d.inst = ref
        coll.foreach(cls.get_typed_referring_object_instance_helper, d)
        return d.list

    def get_referrers(self):
        d = ReferringObjectHelper()
        d.list = []
        d.inst = self
        self.book.foreach_collection(self.get_referring_objects_helper, d)
        return d.list
