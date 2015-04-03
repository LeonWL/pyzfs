
CDEF = """
    enum lzc_send_flags { ... };
    typedef enum {
        DMU_OST_NONE,
        DMU_OST_META,
        DMU_OST_ZFS,
        DMU_OST_ZVOL,
        DMU_OST_OTHER,
        DMU_OST_ANY,
        DMU_OST_NUMTYPES
    } dmu_objset_type_t;

    int libzfs_core_init(void);
    void libzfs_core_fini(void);

    int lzc_snapshot(nvlist_t *, nvlist_t *, nvlist_t **);
    int lzc_create(const char *, dmu_objset_type_t, nvlist_t *);
    int lzc_clone(const char *, const char *, nvlist_t *);
    int lzc_destroy_snaps(nvlist_t *, boolean_t, nvlist_t **);
    int lzc_bookmark(nvlist_t *, nvlist_t **);
    int lzc_get_bookmarks(const char *, nvlist_t *, nvlist_t **);
    int lzc_destroy_bookmarks(nvlist_t *, nvlist_t **);

    int lzc_snaprange_space(const char *, const char *, uint64_t *);

    int lzc_hold(nvlist_t *, int, nvlist_t **);
    int lzc_release(nvlist_t *, nvlist_t **);
    int lzc_get_holds(const char *, nvlist_t **);

    int lzc_send(const char *, const char *, int, enum lzc_send_flags);
    int lzc_receive(const char *, nvlist_t *, const char *, boolean_t, int);
    int lzc_send_space(const char *, const char *, uint64_t *);

    boolean_t lzc_exists(const char *);

    int lzc_rollback(const char *, char *, int);
"""

SOURCE = """
#include <libzfs/libzfs_core.h>
"""

LIBRARY = "zfs_core"

# vim: softtabstop=4 tabstop=4 expandtab shiftwidth=4
