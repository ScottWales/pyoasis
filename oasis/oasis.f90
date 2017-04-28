!> 
!! Copyright 2017 ARC Centre of Excellence for Climate Systems Science
!!
!! \author  Scott Wales <scott.wales@unimelb.edu.au>
!!
!! Licensed under the Apache License, Version 2.0 (the "License");
!! you may not use this file except in compliance with the License.
!! You may obtain a copy of the License at
!!
!!     http://www.apache.org/licenses/LICENSE-2.0
!!
!! Unless required by applicable law or agreed to in writing, software
!! distributed under the License is distributed on an "AS IS" BASIS,
!! WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
!! See the License for the specific language governing permissions and
!! limitations under the License.

module port_status
    use mod_oasis_parameters
    integer, parameter :: notdef = oasis_notdef
    integer, parameter :: var_uncpl = oasis_var_uncpl
    integer, parameter :: out = oasis_out
    integer, parameter :: in = oasis_in
    integer, parameter :: inout = oasis_inout
    integer, parameter :: recvd = oasis_recvd
    integer, parameter :: sent = oasis_sent
    integer, parameter :: locTrans = oasis_locTrans
    integer, parameter :: toRest = oasis_toRest
    integer, parameter :: output = oasis_output
    integer, parameter :: sentOut = oasis_sentOut
    integer, parameter :: toRestOut = oasis_toRestOut
    integer, parameter :: fromRest = oasis_fromRest
    integer, parameter :: input = oasis_input
    integer, parameter :: recvOut = oasis_recvOut
    integer, parameter :: fromRestOut = oasis_fromRestOut
    integer, parameter :: waitGroup = oasis_waitGroup
end module

module types
    use mod_oasis_parameters
    integer, parameter :: real = oasis_real
    integer, parameter :: double = oasis_double
end module

module oasis
contains

   SUBROUTINE init_comp(compid,name)
       use mod_oasis
       implicit none
       integer, intent(out) :: compid
       character(len=80), intent(in) :: name
       compid = -1
       call oasis_init_comp(compid, name)
   end subroutine

   subroutine terminate()
       use mod_oasis
       implicit none
       call oasis_terminate()
    end subroutine

    subroutine abort(compid, routine_name, abort_message, rcode)
        use mod_oasis
        implicit none
        integer, intent(in) :: compid
        character(len=*), intent(in) :: routine_name, abort_message
        integer, intent(in) :: rcode
        call oasis_abort(compid, routine_name, abort_message, rcode)
    end subroutine

    subroutine def_partition(il_part_id, ig_paral, ierror, isize, name)
        use mod_oasis
        implicit none
        integer, intent(out) :: il_part_id
        integer, intent(in) :: ig_paral(:)
        integer, intent(out) :: ierror
        integer, intent(in), optional :: isize
        character(len=120), intent(in), optional :: name
        call oasis_def_partition(il_part_id, ig_paral, ierror, isize, name)
    end subroutine

    subroutine def_var(var_id, name, il_part_id, var_nodims, kinout, var_actual_shape, var_type, ierror)
        use mod_oasis
        implicit none
        integer, intent(out) :: var_id
        character(len=80), intent(in) :: name
        integer, intent(in) :: il_part_id
        integer, intent(in) :: var_nodims(2)
        integer, intent(in) :: kinout
        integer, intent(in) :: var_actual_shape(:)
        integer, intent(in) :: var_type
        integer, intent(out) :: ierror
        call oasis_def_var(var_id, name, il_part_id, var_nodims, kinout, var_actual_shape, var_type, ierror)
    end subroutine

    subroutine put_14(var_id, date, fld1, info, fld2, fld3, fld4, fld5)
        use mod_oasis
        implicit none
        integer, intent(in) :: var_id
        integer, intent(in) :: date
        real(kind=4), intent(in) :: fld1(:)
        integer, intent(out) :: info
        real(kind=4), intent(in), optional :: fld2(:), fld3(:), fld4(:), fld5(:)
        call oasis_put(var_id, date, fld1, info, fld2, fld3, fld4, fld5)
    end subroutine
    subroutine put_18(var_id, date, fld1, info, fld2, fld3, fld4, fld5)
        use mod_oasis
        implicit none
        integer, intent(in) :: var_id
        integer, intent(in) :: date
        real(kind=8), intent(in) :: fld1(:)
        integer, intent(out) :: info
        real(kind=8), intent(in), optional :: fld2(:), fld3(:), fld4(:), fld5(:)
        call oasis_put(var_id, date, fld1, info, fld2, fld3, fld4, fld5)
    end subroutine
    subroutine put_24(var_id, date, fld1, info, fld2, fld3, fld4, fld5)
        use mod_oasis
        implicit none
        integer, intent(in) :: var_id
        integer, intent(in) :: date
        real(kind=4), intent(in) :: fld1(:,:)
        integer, intent(out) :: info
        real(kind=4), intent(in), optional :: fld2(:,:), fld3(:,:), fld4(:,:), fld5(:,:)
        call oasis_put(var_id, date, fld1, info, fld2, fld3, fld4, fld5)
    end subroutine
    subroutine put_28(var_id, date, fld1, info, fld2, fld3, fld4, fld5)
        use mod_oasis
        implicit none
        integer, intent(in) :: var_id
        integer, intent(in) :: date
        real(kind=8), intent(in) :: fld1(:,:)
        integer, intent(out) :: info
        real(kind=8), intent(in), optional :: fld2(:,:), fld3(:,:), fld4(:,:), fld5(:,:)
        call oasis_put(var_id, date, fld1, info, fld2, fld3, fld4, fld5)
    end subroutine

    subroutine get_14(var_id, date, fld, info)
        use mod_oasis
        implicit none
        integer, intent(in) :: var_id
        integer, intent(in) :: date
        real(kind=4), intent(out) :: fld(:)
        integer, intent(out) :: info
        call oasis_put(var_id, date, fld, info)
    end subroutine
    subroutine get_18(var_id, date, fld, info)
        use mod_oasis
        implicit none
        integer, intent(in) :: var_id
        integer, intent(in) :: date
        real(kind=8), intent(out) :: fld(:)
        integer, intent(out) :: info
        call oasis_put(var_id, date, fld, info)
    end subroutine
    subroutine get_24(var_id, date, fld, info)
        use mod_oasis
        implicit none
        integer, intent(in) :: var_id
        integer, intent(in) :: date
        real(kind=4), intent(out) :: fld(:,:)
        integer, intent(out) :: info
        call oasis_put(var_id, date, fld, info)
    end subroutine
    subroutine get_28(var_id, date, fld, info)
        use mod_oasis
        implicit none
        integer, intent(in) :: var_id
        integer, intent(in) :: date
        real(kind=8), intent(out) :: fld(:,:)
        integer, intent(out) :: info
        call oasis_put(var_id, date, fld, info)
    end subroutine
end module
